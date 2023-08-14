# Translation
This looks it is going to be the first big refactor. Due to how matrix vector
multiplication works using numpy, using namedtuples for the Tuples (vector & point) 
may be a poor design choice.

BBIAB

Err, nevermind. Given
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
    assert_array_equal(dot(context.globals[a], context.tuples[b]), context.tuples[c])
```
and that looks fine.