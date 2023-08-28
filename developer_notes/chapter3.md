# Introduction
Biggest diversion from the intent of the book: I am using numpy for
the matrix operations. Two reasons:
1. I have done matrix implementations many times, in C++, Java, Typescript
2. Numpy is the (almost?) standard way of doing linear algebra in Python

Really, numpy is at the core of why Python is popular in production code (
its popularity in education is for different reasons). Learning numpy while
doing the project is going to be the biggest benefit to me. Secondary benefits
will be learning pythonic code better, the behave framework, some github
actions, and other miscellaneous skills.

## Behave
A bit of oddity here. The parser for JetBrains PyCharm and
Behave don't agree. Perhaps because I use 
```gherkin
use_step_matcher("parse")
```
?

Anyway, for 
```gherkin
Given the following 4x4 matrix M:
  | 1    | 2    | 3    | 4    |
  | 5.5  | 6.5  | 7.5  | 8.5  |
  | 9    | 10   | 11   | 12   |
  | 13.5 | 14.5 | 15.5 | 16.5 |
```

```gherkin
@then("inverse({:id}) is the following 4x4 matrix")
```
matches for Behave, but 
```gherkin
@then("inverse({:id}) is the following 4x4 matrix:")
```
matches for PyCharm (no warning nag)

By putting both annotations on the step, both are happy.
It looks wierd though:
```gherkin
@then("inverse({:id}) is the following 4x4 matrix")
@then("inverse({:id}) is the following 4x4 matrix:")
def step_impl(context, a):
    assert_array_approximately_equal(inverse(context.globals[a]), create_table_from(context))
```