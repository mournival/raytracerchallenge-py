from behave import then

from color import blue, green, red
from features.environment import assert_approximately_equal, assert_equal, register_custom_parsers
from tuple import w, x, y, z, is_point, is_vector

register_custom_parsers()


@then("{:id}.a = {:id}")
def step_a_equals_val(context, name, c):
    actual = context.scenario_vars[name].a
    expected = context.scenario_vars[c]
    assert_approximately_equal(actual, expected), f"{ actual = }, expected {expected})"


@then("{:id}.b = {:id}")
def step_b_equals_val(context, name, c):
    actual = context.scenario_vars[name].b
    expected = context.scenario_vars[c]
    assert_approximately_equal(actual, expected), f"{ actual = }, expected {expected})"


@then("{:id}.w = {:rn}")
def step_w_equals_val(context, name, expected):
    assert_approximately_equal(w(context.scenario_vars[name]), expected)


@then("{:id}.x = {:rn}")
def step_x_equals_val(context, name, expected):
    assert_approximately_equal(x(context.scenario_vars[name]), expected)


@then("{:id}.y = {:rn}")
def step_y_equals_val(context, name, expected):
    assert_approximately_equal(y(context.scenario_vars[name]), expected)


@then("{:id}.z = {:rn}")
def step_z_equals_val(context, name, expected):
    assert_approximately_equal(z(context.scenario_vars[name]), expected)


@then("{:id}.blue = {:rn}")
def step_blue_equals_val(context, name, expected):
    assert_approximately_equal(blue(context.scenario_vars[name]), expected)


@then("{:id}.green = {:rn}")
def step_green_equals_val(context, name, expected):
    assert_approximately_equal(green(context.scenario_vars[name]), expected)


@then("{:id}.red = {:rn}")
def step_red_equals_val(context, name, expected):
    assert_approximately_equal(red(context.scenario_vars[name]), expected)


@then("-{:id} = {:op}({:rns})")
def step_negate_equals_op4_vals(context, name, op, params):
    assert_equal(-context.scenario_vars[name], op(*params))


@then("{:id} - {:id} = {:op}({:rns})")
def step_subtraction_equals_op3_vals(context, a, b, dtype, p):
    assert_approximately_equal(context.scenario_vars[a] - context.scenario_vars[b], dtype(*p))


@then("{:id} * {:rn} = {:op}({:rns})")
def step_scalar_multiplication_equals_op4_vals(context, a, c, op, params):
    assert_equal(context.scenario_vars[a] * c, op(*params))


@then("{:id} / {:rn} = {:op}({:rns})")
def step_scalar_division_equals_op4_vals(context, a, c, op, params):
    assert_equal(context.scenario_vars[a] / c, op(*params))


@then("{:id} {:isnota} point")
def step_test_is_point(context, name, is_or_not):
    assert_equal(is_point(context.scenario_vars[name]),
                 is_or_not), f"{is_point(context.scenario_vars[name]) = }, expected {is_or_not} point"


@then("{:id} {:isnota} vector")
def step_test_is_vector(context, name, is_or_not):
    assert_equal(is_vector(context.scenario_vars[name]),
                 is_or_not), f"{is_vector(context.scenario_vars[name]) = }, expected {is_or_not} vector"


@then("{:op}({:id}) = approximately {:rn}")
def step_operation_approximately_equals_val(context, op, a, expected):
    assert_equal(op(context.scenario_vars[a]), expected)


@then("{:op}({:id}) = approximately {:op}({:rns})")
def step_op1_id_approximate_equals_op3_val(context, op, v, dtype, params):
    assert_approximately_equal(op(context.scenario_vars[v]), dtype(*params))
