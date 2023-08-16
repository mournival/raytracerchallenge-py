# Translation
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
@then("{:l} * {:l} = {:l}")
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
tag for the custom parse method, the stepf function that matches
```gherkin
   Then half_quarter * p = point(0, √2/2, √2/2)
    And full_quarter * p = point(0, 0, 1)
```
is
```gherkin
@then("{:l} * {:l} = point({:g}, {:rn}, {:rn})")
def step_matrix_translate_with_radicals_alt1_point_approximately_equals(context, a, b, x, y, z):
    assert_array_approximately_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), point(x, y, z))
```