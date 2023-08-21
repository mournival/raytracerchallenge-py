from behave import use_step_matcher, given, then, step, register_type

from color import color
from features.environment import assert_equal, assert_approximately_equal, parse_ratio, parse_id, parse_matrix_name, \
    parse_operation, parse_radians, assert_array_equal, assert_array_approximately_equal, assert_array_not_equal, \
    create_table_from
from matrix import transpose, dot, submatrix, invertible, inverse, rotation_x, rotation_y, rotation_z, shearing
from tuple import tuple_trtc

use_step_matcher("parse")
register_type(rad=parse_radians)
register_type(id=parse_id)
register_type(mn=parse_matrix_name)
register_type(op=parse_operation)
register_type(rn=parse_ratio)


@given("{:mn}")
def step_matrix_create_empty_n_m(context, name):
    context.scenario_vars[name] = create_table_from(context)


@given("{:id} ← transpose({:id})")
def step_matrix_create_transpose(context, a, b):
    context.scenario_vars[a] = transpose(context.scenario_vars[b])


@step("{:id} is invertible")
def step_matrix_is_invertible(context, a):
    assert (invertible(context.scenario_vars[a]))


@step("{:id} is not invertible")
def step_matrix_is_not_invertible(context, a):
    assert (not invertible(context.scenario_vars[a]))


@step("{:id} ← {:id} * {:id}")
def step_matrix_create_product(context, c, a, b):
    context.scenario_vars[c] = dot(context.scenario_vars[a], context.scenario_vars[b])


@step("{:id} ← {:id} * {:id} * {:id}")
def step_matrix_create_chained_product(context, t, a, b, c):
    context.scenario_vars[t] = dot(dot(context.scenario_vars[a], context.scenario_vars[b]), context.scenario_vars[c])


@step("{:id} ← rotation_x({:rad})")
def step_matrix_create_rotation_x(context, c, radians):
    context.scenario_vars[c] = rotation_x(radians)


@step("{:id} ← rotation_y({:rad})")
def step_matrix_create_rotation_y(context, c, radians):
    context.scenario_vars[c] = rotation_y(radians)


@step("{:id} ← rotation_z({:rad})")
def step_matrix_create_rotation_z(context, c, radians):
    context.scenario_vars[c] = rotation_z(radians)


@step("{:id} ← shearing({:g}, {:g}, {:g}, {:g}, {:g}, {:g})")
def step_matrix_create_shearing(context, c, x_y, x_z, y_x, y_z, z_x, z_y):
    context.scenario_vars[c] = shearing(x_y, x_z, y_x, y_z, z_x, z_y)


@step("{:id} ← inverse({:id})")
def step_matrix_create_inverse(context, b, a):
    context.scenario_vars[b] = inverse(context.scenario_vars[a])


@step("{:id} ← submatrix({:id}, {:d}, {:d})")
def step_matrix_create_submatrix(context, b, a, m, n):
    context.scenario_vars[b] = submatrix(context.scenario_vars[a], m, n)


@then("{:id}[{:d},{:d}] = {:g}")
def step_matrix_element_equals(context, name, r, c, expected):
    assert_equal(context.scenario_vars[name][r, c], expected)


@then("{:id}[{:d},{:d}] = {:rn}")
def step_matrix_element_approximately_equals(context, name, r, c, expected):
    assert_approximately_equal(context.scenario_vars[name][r, c], expected)


@then("{:id} = {:id}")
def step_matrix_equals(context, a, b):
    assert_array_equal(context.scenario_vars[a], context.scenario_vars[b])


@then("{:id} * {:id} = {:id}")
def step_matrix_tuple_multiplication_equals(context, a, b, c):
    assert_array_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), context.scenario_vars[c])


@then("{:id} * {:id} = {:op}({:rn}, {:rn}, {:rn})")
@then("{:id} * {:id} = {:op}({:g}, {:g}, {:g})")
def step_matrix_point_multiplication_equals(context, a, b, dtype, x, y, z):
    if dtype == color:
        actual = context.scenario_vars[a] * context.scenario_vars[b]
    else:
        actual = dot(context.scenario_vars[a], context.scenario_vars[b])
    assert_array_approximately_equal(actual, dtype(x, y, z))


@then("{:id} != {:id}")
def step_matrix_not_equals(context, a, b):
    assert_array_not_equal(context.scenario_vars[a], context.scenario_vars[b])


@then("{:id} * {:id} is the following 4x4 matrix")
@then("{:id} * {:id} is the following 4x4 matrix:")
def step_matrix_multiplication_equals(context, a, b):
    assert_array_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), create_table_from(context))


@then("{:id} is the following 4x4 matrix")
@then("{:id} is the following 4x4 matrix:")
def step_matrix_create_4x4_matrix(context, a):
    assert_array_approximately_equal(context.scenario_vars[a], create_table_from(context))


@then("{:op}({:id}) is the following matrix")
@then("{:op}({:id}) is the following matrix:")
@then("{:op}({:id}) is the following 4x4 matrix")
@then("{:op}({:id}) is the following 4x4 matrix:")
def step_matrix_transpose_approximately_equal(context, operation, a):
    assert_array_approximately_equal(operation(context.scenario_vars[a]), create_table_from(context))


@then("{:op}({:id}, {:d}, {:d}) = {:g}")
def step_matrix_factor_equals(context, operation, a, r, c, expected):
    assert_approximately_equal(operation(context.scenario_vars[a], r, c), expected)


@then("{:op}({:id}) = {:g}")
def step_matrix_determinant_equals(context, operation, a, expected):
    assert_approximately_equal(operation(context.scenario_vars[a]), expected)


@then("{:id} * {:id} = tuple({:g}, {:g}, {:g}, {:g})")
def step_matrix_tuple_dot_product_equals(context, a, b, x, y, z, w):
    assert_array_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), tuple_trtc(x, y, z, w))


@then("submatrix({:id}, {:d}, {:d}) is the following {}x{} matrix")
@then("submatrix({:id}, {:d}, {:d}) is the following {}x{} matrix:")
def step_matrix_submatrix_equals(context, a, m, n, _m, _n):
    assert_array_equal(submatrix(context.scenario_vars[a], m, n), create_table_from(context))


@then("{:id} * {:op}({:id}) = {:id}")
def step_matrix_inverse_multiplication_equals(context, c, operation, b, a):
    actual = dot(context.scenario_vars[c], operation(context.scenario_vars[b]))
    assert_array_approximately_equal(actual, context.scenario_vars[a])
