from behave import use_step_matcher, given, when, then, register_type

from color import Color
from features.environment import assert_equal, parse_ratio, parse_operation, assert_approximately_equal, parse_id
from tuple import Tuple, vector

use_step_matcher("parse")
register_type(id=parse_id)
register_type(rn=parse_ratio)
register_type(op=parse_operation)


@given('{:id} ← tuple({:g}, {:g}, {:g}, {:g})')
def step_tuple_create(context, a, x, y, z, w):
    context.scenario_vars[a] = Tuple(x, y, z, w)


@given("{:id} ← {:op}({:rn}, {:rn}, {:rn})")
def step_tuple_create_vector_with_radicals(context, name, dtype, x, y, z):
    context.scenario_vars[name] = dtype(x, y, z)


@given("{:id} ← {:op}({:g}, {:g}, {:g})")
def step_tuple_create_typed_tuple(context, c, dtype, r, g, b):
    context.scenario_vars[c] = dtype(r, g, b)


@when("{:id} ← {:op}({:id})")
def step_tuple_create_derived(context, a, operation, v):
    context.scenario_vars[a] = operation(context.scenario_vars[v])


@then("{:id} is a point")
def step_tuple_is_point(context, name):
    assert context.scenario_vars[name].is_point(), f"{context.scenario_vars[name]} is NOT a point"


@then("{:id} is not a vector")
def step_tuple_is_not_vector(context, name):
    assert ~context.scenario_vars[name].is_vector(), f"{context.scenario_vars[name]} is a vector"


@then("{:id} is not a point")
def step_tuple_is_not_point(context, name):
    assert ~context.scenario_vars[name].is_point(), f"{context.scenario_vars[name]} is a point"


@then("{:id} is a vector")
def step_tuple_is_vector(context, name):
    assert context.scenario_vars[name].is_vector(), f"{context.scenario_vars[name]} is NOT a vector"


@then("{:id}.{:id} = {:g}")
def step_tuple_field_equals(context, name, field, expected):
    assert context.scenario_vars[name].__getattribute__(
        field) == expected, f"{context.scenario_vars[name].__getattribute__(field).field} != {expected}"


@then("-{:id} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_negate(context, name, x, y, z, w):
    assert_equal(-context.scenario_vars[name], Tuple(x, y, z, w))


@then("{:id} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_equals(context, name, x, y, z, w):
    assert_equal(context.scenario_vars[name], Tuple(x, y, z, w))


@then("{:id} + {:id} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_addition(context, a, b, x, y, z, w):
    assert_equal(context.scenario_vars[a] + context.scenario_vars[b], Tuple(x, y, z, w))


@then("{:id} - {:id} = {:op}({:g}, {:g}, {:g})")
def step_tuple_subtraction_equals(context, a, b, dtype, x, y, z):
    expected = dtype(x, y, z)
    actual = context.scenario_vars[a] - context.scenario_vars[b]
    difference = actual - expected
    assert (difference[0] < 0.0001), f"{actual} !~ {expected}"
    assert (difference[1] < 0.0001), f"{actual} !~ {expected}"
    assert (difference[2] < 0.0001), f"{actual} !~ {expected}"
    if dtype != Color:
        assert (difference[3] < 0.0001), f"{actual} !~ {expected}"


@then("{:id} * {:g} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_scalar_multiplication(context, a, c, x, y, z, w):
    assert_equal(context.scenario_vars[a] * c, Tuple(x, y, z, w))


@then("{:id} / {:g} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_scalar_division(context, a, c, x, y, z, w):
    assert_equal(context.scenario_vars[a] / c, Tuple(x, y, z, w))


@then("{:op}({:id}) = {:rn}")
def step_tuple_operation_equals(context, operation, a, expected):
    assert_equal(operation(context.scenario_vars[a]), expected)


@then("{:op}({:id}) = approximately {:g}")
def step_tuple_operation_approximately_equals(context, operation, a, expected):
    assert_equal(operation(context.scenario_vars[a]), expected)


@then("{:op}({:id}) = {:op}({:g}, {:g}, {:g})")
def step_tuple_operations_equal(context, operation, v, dtype, x, y, z):
    assert_equal(operation(context.scenario_vars[v]), dtype(x, y, z))


@then("{:op}({:id}) = approximately vector({:g}, {:g}, {:g})")
def step_tuple_normalized_approximately_equals(context, operation, v, x, y, z):
    actual = operation(context.scenario_vars[v])
    assert_approximately_equal(actual.x, x)
    assert_approximately_equal(actual.y, y)
    assert_approximately_equal(actual.z, z)


@then("{:op}({:id}, {:id}) = {:g}")
def step_tuple_operation_scalar_equals(context, operation, a, b, expected):
    assert_equal(operation(context.scenario_vars[a], context.scenario_vars[b]), expected)


@then("{:op}({:id}, {:id}) = vector({:g}, {:g}, {:g})")
def step_tuple_binary_operation_equals(context, operation, a, b, x, y, z):
    assert_equal(operation(context.scenario_vars[a], context.scenario_vars[b]), vector(x, y, z))


@then("{:id} = {:op}({:g}, {:g}, {:g})")
def step_tuple_equal(context, v, dtype, x, y, z):
    assert_equal(context.scenario_vars[v], dtype(x, y, z))


@then("{:id} = approximately {:op}({:g}, {:g}, {:g})")
def step_tuple_approximately_equal(context, v, dtype, x, y, z):
    expected = dtype(x, y, z)
    actual = context.scenario_vars[v]
    difference = actual - expected
    assert (difference[0] < 0.0001), f"{actual} !~ {expected}"
    assert (difference[1] < 0.0001), f"{actual} !~ {expected}"
    assert (difference[2] < 0.0001), f"{actual} !~ {expected}"
    if dtype != Color:
        assert (difference[3] < 0.0001)


@then("{:id} + {:id} = color({:g}, {:g}, {:g})")
def step_tuple_color_addition(context, a, b, red, green, blue):
    assert_equal(context.scenario_vars[a] + context.scenario_vars[b], Color(red, green, blue))


@then("{:id} * {:g} = color({:g}, {:g}, {:g})")
def step_tuple_color_scaling(context, a, b, red, green, blue):
    actual = context.scenario_vars[a] * float(b)
    assert_approximately_equal(actual.red, red)
    assert_approximately_equal(actual.green, green)
    assert_approximately_equal(actual.blue, blue)
