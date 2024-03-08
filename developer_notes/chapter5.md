# Chapter 5: Ray-Sphere Intersections

Started with the first 2 intersection tests, then off to refactoring land.
Cleaned up the tests:

- converted operation parser to return lambdas for some of the named tuple element access as these are really just
  step_def helpers
- reworked a number of the step defs, removing essentially redundant one once operation parser was improved

Overall, the tests and the implementation are starting to look very domain like:

tuple_steps:

```python
from behave import then
from features.environment import assert_equal

@then("{:id} = {:op}({:g}, {:g}, {:g}, {:g})")
def step_tuple_equals(context, name, op, x, y, z, w):
    assert_equal(context.scenario_vars[name], op(x, y, z, w))


@then("{:id} + {:id} = {:op}({:g}, {:g}, {:g})")
def step_tuple_color_addition(context, a, b, op, x, y, zl):
    assert_equal(context.scenario_vars[a] + context.scenario_vars[b], op(x, y, zl))
```

ray.pl:

```python
from collections import namedtuple

ray = namedtuple('Ray', 'origin direction')


def position(r, t):
    return r.origin + r.direction * t

```

## ASIDE

Hmm, just learned about [data classes](https://peps.python.org/pep-0557/#abstract) (vs. named tuple ... )

Probably should have used those for color / tuple. Well, color at least. Using the numpy.array types for tuple and
matrix probably makes the most since due to the dot / cross / matmul / mat div / det / yada that numpy provides.

## Whew!

Not much app code, but a huge amount of testing code refactoring. Doing fine until:

```gherkin
  Scenario: A sphere's default transformation
    Given s ← sphere()
    Then s.transform = identity_matrix

```

as this

```gherkin
    Then s.transform = identity_matrix
```

caused a name class with

```gherkin
Scenario: Translating a ray
  Given r ← ray(point(1, 2, 3), vector(0, 1, 0))
    And m ← translation(3, 4, 5)
  When r2 ← transform(r, m)
  Then r2.origin = point(4, 6, 8)
    And r2.direction = vector(0, 1, 0)
```

Specifically,

```gherkin
  When r2 ← transform(r, m)
```

That is, a field in the sphere (shape class), and an important operation had the same name.

After a lot of refactoring, came to the conclusion that field names and operation / function names needed to be
separate.
Fortunately, combining the "." in the field parsing allowed a straight forward manner of disambiguation:

```python
from behave import use_step_matcher, then, step, register_type

from features.environment import assert_equal, parse_operation, parse_id, parse_field

use_step_matcher("parse")
register_type(field=parse_field)
register_type(id=parse_id)
register_type(op=parse_operation)

@then("{:id}{:field} = {:id}")
def step_tuple_field_equals_var(context, name, field, expected):
    assert_equal(field(context.scenario_vars[name]), context.scenario_vars[expected])

@step("{:id} ← {:op}({:g}, {:id})")
def step_tuple_create_intersection(context, name, dtype, t, o):
    context.scenario_vars[name] = dtype(t, context.scenario_vars[o])
```

And I learned some things about [pypi parse](https://pypi.org/project/parse/):

> A more complete example of a custom type might be:
> ```python
> from parse import with_pattern
>
> yesno_mapping = {
>      "yes":  True,   "no":    False,
>      "on":   True,   "off":   False,
>      "true": True,   "false": False,
>  }
> @with_pattern(r"|".join(yesno_mapping))
> def parse_yesno(text):
>     return yesno_mapping[text.lower()]
> ```

Which lead to consolidating the field and operation custom parsers into code like:

```python
from color import blue, green, red
from parse import with_pattern
from tuple import w, x, y, z

fields_mapping = {
  '.blue': blue,
  '.count': lambda lx: len(lx),
  '.direction': lambda r: r.direction,
  '.green': green,
  '.height': lambda c: c.height,
  '.object': lambda ob: ob.object,
  '.origin': lambda ob: ob.origin,
  '.red': red,
  '.t': lambda i: i.t,
  '.transform': lambda o: o.transform,
  '.w': w,
  '.width': lambda c: c.width,
  '.x': x,
  '.y': y,
  '.z': z,
}


@with_pattern(r"|".join(fields_mapping))
def parse_field(text):
  return fields_mapping[text]
```

Overall, I really like where this refactoring went. The step function are really functions, and only the setter (*
*context.scenario_vars[name] =** ) have side effects.
And the step implementation looks like a fairly obvious (functional) translation of the behave pattern:

```python
from behave import use_step_matcher, then, register_type

from features.environment import assert_equal, parse_operation, parse_id, parse_field

use_step_matcher("parse")
register_type(field=parse_field)
register_type(id=parse_id)
register_type(op=parse_operation)

@then("{:id}{:field} = {:id}")
def step_tuple_field_equals_var(context, name, field, expected):
    assert_equal(field(context.scenario_vars[name]), context.scenario_vars[expected])
```

And to add new field or operation, only a new entry needs to be entered in the _mapping dictionary, so easy to extend (
for now).