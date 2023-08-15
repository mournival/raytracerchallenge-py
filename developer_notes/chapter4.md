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
``` gherkin
    Then inv * p = point(0, √2/2, -√2/2)
```
and all the matrix and vector multiplications and dot products.