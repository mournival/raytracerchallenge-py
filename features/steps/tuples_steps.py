from behave import use_step_matcher, given, then, step, register_type

import matrix
from features.environment import assert_equal, parse_ratio, parse_operation, assert_approximately_equal, parse_id, \
    parse_is_is_not, parse_field
from tuple import is_point, is_vector

use_step_matcher("parse")
register_type(field=parse_field)
register_type(id=parse_id)
register_type(isnota=parse_is_is_not)
register_type(rn=parse_ratio)
register_type(op=parse_operation)


@given('{:id} ← {:op}({:g}, {:g}, {:g}, {:g})')
def step_tuple_create(context, a, op, x, y, z, w):
    context.scenario_vars[a] = op(x, y, z, w)


@given("{:id} ← {:op}({:g}, {:g}, {:g})")
@given("{:id} ← {:op}({:rn}, {:rn}, {:rn})")
def step_tuple_create_vector_with_radicals(context, name, dtype, x, y, z):
    context.scenario_vars[name] = dtype(x, y, z)


@given("{:id} ← {:op}({:g}, {:g}, {:g}) * {:op}({:rad})")
def step_tuple_create_vector_with_radicals(context, name, op1, x1, y1, z1, op2, rad):
    context.scenario_vars[name] = matrix.dot(op1(x1, y1, z1), op2(rad))


@given("{:id} ← {:op}({:op}({:rn}, {:rn}, {:rn}), {:op}({:rn}, {:rn}, {:rn}))")
@given("{:id} ← {:op}({:op}({:rn}, {:d}, {:d}), {:op}({:d}, {:d}, {:d}))")
def step_tuple_create_vector_binary_op_with_radicals(context, name, op1, op2, x2, y2, z2, op3, x3, y3, z3):
    context.scenario_vars[name] = op1(op2(x2, y2, z2), op3(x3, y3, z3))


@step("{:id} ← {:op}({:g}, {:id})")
def step_tuple_create_intersection(context, name, dtype, t, o):
    context.scenario_vars[name] = dtype(t, context.scenario_vars[o])


@step("{:id} ← {:op}({:id}, {:id})")
def step_tuple_create_derived(context, a, op, u, v):
    context.scenario_vars[a] = op(context.scenario_vars[u], context.scenario_vars[v])


@step("{:id} ← {:op}({:id}, {:id}, {:id}, {:id})")
def step_tuple_create_derived_tuple(context, a, op, w, x, y, z):
    context.scenario_vars[a] = op(context.scenario_vars[w], context.scenario_vars[x], context.scenario_vars[y],
                                  context.scenario_vars[z])


@then("{:id} is nothing")
def step_item_is_none(context, name):
    assert context.scenario_vars[name] is None, f"Actual {context.scenario_vars[name] =}, expected None"


@then("{:id} {:isnota} point")
def step_tuple_test_is_point(context, name, is_or_not):
    assert_equal(is_point(context.scenario_vars[name]), is_or_not)


@then("{:id} {:isnota} vector")
def step_tuple_test_is_vector(context, name, is_or_not):
    assert_equal(is_vector(context.scenario_vars[name]), is_or_not)


@then("{:id}{:field} = {:op}({:g}, {:g}, {:g})")
def step_tuple_field_equals_op(context, name, field, op, x, y, z):
    assert_equal(field(context.scenario_vars[name]), op(x, y, z))


@then("{:id}[{:d}]{:field} = {:g}")
def step_tuple_array_element_field_equals_val(context, name, i, field, expected):
    assert_equal(field(context.scenario_vars[name][i]), expected)


@then("{:id}[{:d}]{:field} = {:id}")
def step_tuple_array_element_field_equals_var(context, name, i, field, expected):
    assert_equal(field(context.scenario_vars[name][i]), context.scenario_vars[expected])


@then("{:id}{:field} = {:id}")
def step_tuple_field_equals_var(context, name, field, expected):
    assert_equal(field(context.scenario_vars[name]), context.scenario_vars[expected])


@then("{:id}{:field} = {:g}")
def step_tuple_field_equals_literal(context, name, field, expected):
    assert_equal(field(context.scenario_vars[name]), expected)


@then("-{:id} = {:op}({:g}, {:g}, {:g}, {:g})")
def step_tuple_negate(context, name, op, x, y, z, w):
    assert_equal(-context.scenario_vars[name], op(x, y, z, w))


@then("{:id} = {:op}({:g}, {:g}, {:g}, {:g})")
def step_tuple_equals(context, name, op, x, y, z, w):
    assert_equal(context.scenario_vars[name], op(x, y, z, w))


@then("{:id} + {:id} = {:op}({:g}, {:g}, {:g}, {:g})")
def step_tuple_addition(context, a, b, op, x, y, z, w):
    assert_equal(context.scenario_vars[a] + context.scenario_vars[b], op(x, y, z, w))


@then("{:id} - {:id} = {:op}({:g}, {:g}, {:g})")
def step_tuple_subtraction_equals(context, a, b, dtype, x, y, z):
    expected = dtype(x, y, z)
    actual = context.scenario_vars[a] - context.scenario_vars[b]
    assert_approximately_equal(actual, expected)


@then("{:id} * {:g} = {:op}({:g}, {:g}, {:g}, {:g})")
def step_tuple_scalar_multiplication(context, a, c, op, x, y, z, w):
    assert_equal(context.scenario_vars[a] * c, op(x, y, z, w))


@then("{:id} / {:g} = {:op}({:g}, {:g}, {:g}, {:g})")
def step_tuple_scalar_division(context, a, c, op, x, y, z, w):
    assert_equal(context.scenario_vars[a] / c, op(x, y, z, w))


@then("{:op}({:id}) = {:rn}")
def step_tuple_operation_equals(context, op, a, expected):
    assert_equal(op(context.scenario_vars[a]), expected)


@then("{:op}({:id}) = approximately {:g}")
def step_tuple_operation_approximately_equals(context, op, a, expected):
    assert_equal(op(context.scenario_vars[a]), expected)


@then("{:op}({:id}) = {:op}({:g}, {:g}, {:g})")
def step_tuple_operations_equal(context, op, v, dtype, x, y, z):
    assert_equal(op(context.scenario_vars[v]), dtype(x, y, z))


@then("{:op}({:id}) = approximately {:op}({:g}, {:g}, {:g})")
def step_tuple_normalized_approximately_equals(context, op, v, dtype, x, y, z):
    assert_approximately_equal(op(context.scenario_vars[v]), dtype(x, y, z))


@then("{:op}({:id}, {:id}) = {:g}")
def step_tuple_operation_scalar_equals(context, op, a, b, expected):
    assert_equal(op(context.scenario_vars[a], context.scenario_vars[b]), expected)


@then("{:op}({:id}, {:id}) = {:op}({:g}, {:g}, {:g})")
def step_tuple_binary_operation_equals(context, op1, a, b, op2, x, y, z):
    assert_equal(op1(context.scenario_vars[a], context.scenario_vars[b]), op2(x, y, z))


@then("{:id} = {:op}({:id})")
def step_tuple_equal(context, a, op, b):
    assert_equal(context.scenario_vars[a], op(context.scenario_vars[b]))


@then("{:id} = {:op}({:rn}, {:rn}, {:rn})")
@then("{:id} = {:op}({:g}, {:g}, {:g})")
def step_tuple_equal(context, v, dtype, x, y, z):
    assert_approximately_equal(context.scenario_vars[v], dtype(x, y, z))


@then("{:id} = approximately {:op}({:g}, {:g}, {:g})")
def step_tuple_approximately_equal(context, v, dtype, x, y, z):
    assert_approximately_equal(context.scenario_vars[v], dtype(x, y, z))


@then("{:id} + {:id} = {:op}({:g}, {:g}, {:g})")
def step_tuple_color_addition(context, a, b, op, r, g, bl):
    assert_equal(context.scenario_vars[a] + context.scenario_vars[b], op(r, g, bl))


@then("{:id} * {:g} = {:op}({:g}, {:g}, {:g})")
def step_tuple_color_scaling(context, a, c, op, r, g, b):
    assert_equal(context.scenario_vars[a] * c, op(r, g, b))

