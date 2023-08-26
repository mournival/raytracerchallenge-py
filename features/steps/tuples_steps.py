from behave import use_step_matcher, given, when, then, register_type

from color import color
from features.environment import assert_equal, parse_ratio, parse_operation, assert_approximately_equal, parse_id
from tuple import tuple_trtc, vector, is_point, is_vector

use_step_matcher("parse")
register_type(id=parse_id)
register_type(rn=parse_ratio)
register_type(op=parse_operation)


@given('{:id} ← tuple({:g}, {:g}, {:g}, {:g})')
def step_tuple_create(context, a, x, y, z, w):
    context.scenario_vars[a] = tuple_trtc(x, y, z, w)


@given("{:id} ← {:op}({:rn}, {:rn}, {:rn})")
def step_tuple_create_vector_with_radicals(context, name, dtype, x, y, z):
    context.scenario_vars[name] = dtype(x, y, z)


@given("{:id} ← {:op}({:op}({:rn}, {:rn}, {:rn}), {:op}({:rn}, {:rn}, {:rn}))")
@given("{:id} ← {:op}({:op}({:rn}, {:d}, {:d}), {:op}({:d}, {:d}, {:d}))")
def step_tuple_create_vector_with_radicals(context, name, op1, op2, x2, y2, z2, op3, x3, y3, z3):
    context.scenario_vars[name] = op1(op2(x2, y2, z2), op3(x3, y3, z3))


@given("{:id} ← {:op}({:g}, {:g}, {:g})")
def step_tuple_create_typed_tuple(context, c, dtype, r, g, b):
    context.scenario_vars[c] = dtype(r, g, b)


@when("{:id} ← {:op}({:id})")
def step_tuple_create_derived(context, a, operation, v):
    context.scenario_vars[a] = operation(context.scenario_vars[v])


@then("{:id} is a point")
def step_tuple_is_point(context, name):
    assert is_point(context.scenario_vars[name]), f"{context.scenario_vars[name]} is NOT a point"


@then("{:id} is not a vector")
def step_tuple_is_not_vector(context, name):
    assert not is_vector(context.scenario_vars[name]), f"{context.scenario_vars[name]} is a vector"


@then("{:id} is not a point")
def step_tuple_is_not_point(context, name):
    assert not is_point(context.scenario_vars[name]), f"{context.scenario_vars[name]} is a point"


@then("{:id} is a vector")
def step_tuple_is_vector(context, name):
    assert is_vector(context.scenario_vars[name]), f"{context.scenario_vars[name]} is NOT a vector"


@then("{:id}.{:op} = {:g}")
def step_tuple_field_equals(context, name, op, expected):
    assert_equal(op(context.scenario_vars[name]), expected)


@then("{:id}.origin = {:id}")
def step_tuple_field_equals(context, name, expected):
    assert_equal(context.scenario_vars[name].origin, context.scenario_vars[expected])


@then("{:id}.origin = {:id}")
def step_tuple_field_equals(context, name, expected):
    assert_equal(context.scenario_vars[name].origin, context.scenario_vars[expected])


@then("-{:id} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_negate(context, name, x, y, z, w):
    assert_equal(-context.scenario_vars[name], tuple_trtc(x, y, z, w))


@then("{:id} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_equals(context, name, x, y, z, w):
    assert_equal(context.scenario_vars[name], tuple_trtc(x, y, z, w))


@then("{:id} + {:id} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_addition(context, a, b, x, y, z, w):
    assert_equal(context.scenario_vars[a] + context.scenario_vars[b], tuple_trtc(x, y, z, w))


@then("{:id} - {:id} = {:op}({:g}, {:g}, {:g})")
def step_tuple_subtraction_equals(context, a, b, dtype, x, y, z):
    expected = dtype(x, y, z)
    actual = context.scenario_vars[a] - context.scenario_vars[b]
    assert_approximately_equal(actual, expected)


@then("{:id} * {:g} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_scalar_multiplication(context, a, c, x, y, z, w):
    assert_equal(context.scenario_vars[a] * c, tuple_trtc(x, y, z, w))


@then("{:id} / {:g} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_scalar_division(context, a, c, x, y, z, w):
    assert_equal(context.scenario_vars[a] / c, tuple_trtc(x, y, z, w))


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
    assert_approximately_equal(operation(context.scenario_vars[v]), vector(x, y, z))


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
    assert_approximately_equal(context.scenario_vars[v], dtype(x, y, z))


@then("{:id} + {:id} = color({:g}, {:g}, {:g})")
def step_tuple_color_addition(context, a, b, r, g, bl):
    assert_equal(context.scenario_vars[a] + context.scenario_vars[b], color(r, g, bl))


@then("{:id} * {:g} = color({:g}, {:g}, {:g})")
def step_tuple_color_scaling(context, a, c, r, g, b):
    assert_equal(context.scenario_vars[a] * c, color(r, g, b))
