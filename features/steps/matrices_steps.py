from behave import use_step_matcher, given, then, step, register_type
from behave.model import Row

from features.environment import assert_equal, assert_approximately_equal, parse_ratio, parse_id, parse_matrix_name, \
    parse_operation
from matrix import eye, matrix, transpose, array_equal, dot, submatrix, invertible, \
    inverse, array_approximately_equal, rotation_x
from tuple import Tuple

use_step_matcher("parse")

register_type(rn=parse_ratio)
register_type(id=parse_id)
register_type(mn=parse_matrix_name)
register_type(op=parse_operation)


@given("{:mn}")
def step_matrix_create_empty_n_m(context, name):
    context.scenario_vars[name] = create_table_from(context)


@given("{:l} ← transpose(identity_matrix)")
def step_matrix_create_transpose(context, a):
    context.scenario_vars[a] = transpose(eye(4))


@step("{:l} is invertible")
def step_matrix_is_invertible(context, a):
    assert (invertible(context.scenario_vars[a]))


@step("{:l} is not invertible")
def step_matrix_is_not_invertible(context, a):
    assert (not invertible(context.scenario_vars[a]))


@step("{:l} ← {:l} * {:l}")
def step_matrix_create_product(context, c, a, b):
    context.scenario_vars[c] = dot(context.scenario_vars[a], context.scenario_vars[b])


@step("{:id} ← rotation_x({:rn})")
def step_matrix_create_rotation_x(context, c, radians):
    context.scenario_vars[c] = rotation_x(radians)


@step("{:l} ← inverse({:w})")
def step_matrix_create_inverse(context, b, a):
    context.scenario_vars[b] = inverse(context.scenario_vars[a])


@step("{:l} ← {:op}({:g}, {:g}, {:g})")
def step_matrix_create_scaling(context, a, operation, x, y, z):
    context.scenario_vars[a] = operation(x, y, z)


@step("{:l} ← submatrix({:l}, {:d}, {:d})")
def step_matrix_create_submatrix(context, b, a, m, n):
    context.scenario_vars[b] = submatrix(context.scenario_vars[a], m, n)


@then("{:w}[{:d},{:d}] = {:g}")
def step_matrix_element_equals(context, name, r, c, expected):
    assert_equal(context.scenario_vars[name][r, c], expected)


@then("{:w}[{:d},{:d}] = {:rn}")
def step_matrix_element_approximately_equals(context, name, r, c, expected):
    assert_approximately_equal(context.scenario_vars[name][r, c], expected)


@then("{:l} = {:l}")
def step_matrix_equals(context, a, b):
    assert_array_equal(context.scenario_vars[a], context.scenario_vars[b])


@then("{:l} * {:l} = {:l}")
def step_matrix_tuple_multiplication_equals(context, a, b, c):
    assert_array_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), context.scenario_vars[c])


@then("{:id} * {:l} = {:op}({:g}, {:rn}, {:rn})")
@then("{:l} * {:l} = {:op}({:g}, {:rn}, {:rn})")
@then("{:id} * {:l} = {:op}({:g}, {:g}, {:g})")
@then("{:l} * {:l} = {:op}({:g}, {:g}, {:g})")
def step_matrix_point_multiplication_equals(context, a, b, dtype, x, y, z):
    assert_array_approximately_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), dtype(x, y, z))

@then("{:l} != {:l}")
def step_matrix_not_equals(context, a, b):
    assert_array_not_equal(context.scenario_vars[a], context.scenario_vars[b])


@then("{:l} * {:l} is the following 4x4 matrix")
@then("{:l} * {:l} is the following 4x4 matrix:")
def step_matrix_multiplication_equals(context, a, b):
    assert_array_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), create_table_from(context))


@then("{:w} is the following 4x4 matrix")
@then("{:w} is the following 4x4 matrix:")
def step_matrix_create_4x4_matrix(context, a):
    assert_array_approximately_equal(context.scenario_vars[a], create_table_from(context))


@then("{:op}({:l}) is the following matrix")
@then("{:op}({:l}) is the following matrix:")
@then("{:op}({:l}) is the following 4x4 matrix")
@then("{:op}({:l}) is the following 4x4 matrix:")
def step_matrix_transpose_approximately_equal(context, operation, a):
    assert_array_approximately_equal(operation(context.scenario_vars[a]), create_table_from(context))


@then("{:l} * identity_matrix = {:l}")
def step_matrix_identity_multiplication(context, a, b):
    a_ = context.scenario_vars[a]
    assert_array_equal(dot(a_, eye(a_.shape[0])), context.scenario_vars[b])


@then("{:l} = identity_matrix")
def step_matrix_equals_identity(context, a):
    m = context.scenario_vars[a]
    assert_array_equal(m, eye(m.shape[0]))


@then("{:op}({:l}, {:d}, {:d}) = {:g}")
def step_matrix_cofactor_equals(context, operation, a, r, c, expected):
    assert_approximately_equal(operation(context.scenario_vars[a], r, c), expected)


@then("{:op}({:l}) = {:g}")
def step_matrix_determinant_equals(context, operation, a, expected):
    assert_approximately_equal(operation(context.scenario_vars[a]), expected)


@then("{:l} * {:l} = tuple({:g}, {:g}, {:g}, {:g})")
def step_matrix_tuple_dot_product_equals(context, a, b, x, y, z, w):
    assert_array_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), Tuple(x, y, z, w))


@then("identity_matrix * {:l} = {:l}")
def step_matrix_identity_tuple_multiplication_equals(context, a, b):
    a_ = context.scenario_vars[a]
    assert_array_equal(dot(eye(4), a_), context.scenario_vars[b])


@then("submatrix({:l}, {:d}, {:d}) is the following {}x{} matrix")
@then("submatrix({:l}, {:d}, {:d}) is the following {}x{} matrix:")
def step_matrix_submatrix_equals(context, a, m, n, _m, _n):
    assert_array_equal(submatrix(context.scenario_vars[a], m, n), create_table_from(context))


@then("{:l} * {:op}({:l}) = {:l}")
def step_matrix_inverse_multiplication_equals(context, c, operation, b, a):
    assert_array_approximately_equal(dot(context.scenario_vars[c], operation(context.scenario_vars[b])),
                                     context.scenario_vars[a])


def assert_array_equal(actual, expected):
    assert array_equal(actual, expected), f"{actual} != {expected}"


def assert_array_approximately_equal(actual, expected):
    assert array_approximately_equal(actual, expected), f"{actual} != {expected}"


def assert_array_not_equal(actual, expected):
    assert not array_equal(actual, expected), f"{actual} = {expected}"


def create_table_from(context):
    heading_row = Row(context.table.headings, context.table.headings)
    table_data = context.table.rows
    table_data.insert(0, heading_row)
    return matrix(table_data)
