# Chapter 4: Matrix Translation
This looks it is going to be the first big refactor. Due to how matrix vector
multiplication works using numpy, using namedtuples for the Tuples (vector & point) 
may be a poor design choice.

BBIAB

Err, never mind. Given
```gherkin
Scenario: Translation does not affect vectors
  Given transform ← translation(5, -3, 2)
    And v ← vector(-3, 4, 5)
   Then transform * v = v
```
the 'Then' step def is

```python
from behave import then
from features.environment import assert_array_equal
from matrix import dot

@then("{:id} * {:id} = {:id}")
def step_impl(context, a, b, c):
    assert_array_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), context.scenario_vars[c])
```
and that looks fine.

## Test parsing
And here is where I begin to think about creating parsing helper utils for the 'special' cases (radicals)
```gherkin
    Then inv * p = point(0, √2/2, -√2/2)
```
and all the matrix and vector multiplications and dot products.

Starting to consider how much time to put into step utility functions.
Some tradeoffs are, lots of simple step vs. potential ambiguities over time.

Some of the parsing, it does make since because the feature files use
non-ascii symbols and rational numbers, e.g.:

```gherkin
  Scenario: Rotating a point around the x axis
    Given p ← point(0, 1, 0)
    And half_quarter ← rotation_x(π / 4)
    And full_quarter ← rotation_x(π / 2)
    Then half_quarter * p = point(0, √2/2, √2/2)
    And full_quarter * p = point(0, 0, 1)
```

Creating a custom number parser probably makes sense, so that, if :rn is the 
tag for the custom parse method, the step function that matches
```gherkin
   Then half_quarter * p = point(0, √2/2, √2/2)
    And full_quarter * p = point(0, 0, 1)
```
is
```gherkin
@then("{:id} * {:id} = point({:g}, {:rn}, {:rn})")
def step_matrix_translate_with_radicals_alt1_point_approximately_equals(context, a, b, x, y, z):
    assert_array_approximately_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), point(x, y, z))
```

## Finished Chapter 4
Fairly large reworking of test code with a small number of new library code:
```python
from math import cos, sin
import numpy as np

def rotation_x(radians):
    return np.array([
        [1, 0, 0, 0], [0, cos(radians), -sin(radians), 0], [0, sin(radians), cos(radians), 0], [0, 0, 0, 1]
    ])


def rotation_y(radians):
    return np.array([
        [cos(radians), 0, sin(radians), 0], [0, 1, 0, 0], [-sin(radians), 0, cos(radians), 0], [0, 0, 0, 1]
    ])


def rotation_z(radians):
    return np.array([
        [cos(radians), -sin(radians), 0, 0], [sin(radians), cos(radians),0, 0], [0, 0, 1, 0], [0, 0, 0, 1]
    ])


def scaling(x, y, z):
    return np.array([[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]])


def shearing(x_y, x_z, y_x, y_z, z_x, z_y):
    return np.array([[1, x_y, x_z, 0], [y_x, 1, y_z, 0], [z_x, z_y, 1, 0], [0, 0, 0, 1]])


#...


def translation(x, y, z):
    return np.array([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]])

```

The (test) environment file had the largest change, as the custom type parsers was a rabbit's warren of paths. Finally got
a settled at:
```python
import math
import re
from parse import with_pattern

@with_pattern(r'π\s/\s\d+')
def parse_radians(text):
    a = text
    m = re.match(r'π / (\d+)$', a)
    if m:
        return math.pi / int(m.groups()[0])
    raise Exception(f"Error parsing {text}")


@with_pattern(r'[a-zA-Z]+_[a-zA-Z]+|[a-zA-Z]+|[acpv]\d')
def parse_id(text):
    return text


@with_pattern(r'\w+')
def parse_operation(text):
    if text == 'cofactor':
        import matrix
        return matrix.cofactor
    if text == 'color':
        from color import Color
        return Color
    if text == 'cross':
        from tuple import cross
        return cross
    if text == 'determinant':
        import matrix
        return matrix.det
    if text == 'dot':
        from tuple import dot
        return dot
    if text == 'inverse':
        import matrix
        return matrix.inverse
    if text == 'magnitude':
        from tuple import magnitude
        return magnitude
    if text == 'minor':
        import matrix
        return matrix.minor
    if text == 'normalize':
        from tuple import normalize
        return normalize
    if text == 'point':
        from tuple import point
        return point
    if text == 'scaling':
        import matrix
        return matrix.scaling
    if text == 'translation':
        import matrix
        return matrix.translation
    if text == 'transpose':
        import matrix
        return matrix.transpose
    if text == 'vector':
        from tuple import vector
        return vector
    raise NotImplementedError(f"{text}")


@with_pattern(r'the following (\dx\d )?matrix \w+:?')
def parse_matrix_name(text):
    m = re.match(r'the following \d?x?\d? ?matrix (\w):?', text)
    return m.groups()[0]
```

The idea was to make the pattern look close to the domain (matrix / vector algebra) in the step file. It looks okay (with some compromises). 
The assignment steps are quite nice:
```python
from behave import step
from matrix import dot, rotation_x

@step("{:id} ← {:id} * {:id}")
def step_matrix_create_product(context, c, a, b):
    context.scenario_vars[c] = dot(context.scenario_vars[a], context.scenario_vars[b])


@step("{:id} ← {:id} * {:id} * {:id}")
def step_matrix_create_product(context, t, a, b, c):
    context.scenario_vars[t] = dot(dot(context.scenario_vars[a], context.scenario_vars[b]), context.scenario_vars[c])


@step("{:id} ← rotation_x({:rad})")
def step_matrix_create_rotation_x(context, c, radians):
    context.scenario_vars[c] = rotation_x(radians)

#...
```

And the operation based ones also seem to work out:
```python
from behave import then
from features.environment import assert_array_equal, assert_array_approximately_equal
from matrix import dot
    
@then("{:id} = {:id}")
def step_matrix_equals(context, a, b):
    assert_array_equal(context.scenario_vars[a], context.scenario_vars[b])


@then("{:id} * {:id} = {:id}")
def step_matrix_tuple_multiplication_equals(context, a, b, c):
    assert_array_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), context.scenario_vars[c])


# OBSOLETE: Refactored out of existence
@then("{:id} * {:id} = {:op}({:rn}, {:rn}, {:rn})")
@then("{:id} * {:id} = {:op}({:g}, {:g}, {:g})")
def step_matrix_point_multiplication_equals(context, a, b, dtype, x, y, z):
    if dtype == Color:
        assert_array_approximately_equal(hadamard_product(context.scenario_vars[a], context.scenario_vars[b]),
                                         dtype(x, y, z))
    else:
        assert_array_approximately_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), dtype(x, y, z))
```

N.B., Color is implemented like Tuple/vector/point, and the steps have a huge structural similarity,
but are not IS-A compatible in the code, so there is a bit of type hackery. May return to this later, but for now it 
does not offend my senses overly much (it does, no simple solution has presented itself).

# Major Refactor
Yanked out custom tuple/color classes, just left api wrappers for np.array

Also implemented the clock demo (thogh it looks more liking an aiming reticle.)
![chatper4.png](..%2Fimages%2Fchapter4.png)