# Intersections

Started with the first 2 intersection tests, then off to refactoring land.
Cleaned up the tests:
- converted operation parser to return lambdas for some of the named tuple element access as these are really just step_def helpers
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

#
Hmm, just learned about [data classes](https://peps.python.org/pep-0557/#abstract) (vs. named tuple ... )

Probably should have used those for color / tuple. Well, color at least. Using the numpy.array types for tuple and matrix probably makes the most since due to the dot / cross / matmul / mat div / det / yada that numpy provides.
