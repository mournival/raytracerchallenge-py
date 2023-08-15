from behave import use_step_matcher, given, then, step, register_type
from behave.model import Row

from features.environment import assert_equal, assert_approximately_equal, parse_ratio
from matrix import eye, det, matrix, transpose, matmul, array_equal, dot, submatrix, minor, cofactor, invertible, \
    inverse, array_approximately_equal, scaling, translation, rotation_x
from tuple import Tuple, point, vector

use_step_matcher("parse")

register_type(rn=parse_ratio)


@given("the following matrix {:w}")
@given("the following matrix {:w}:")
@given("the following 2x2 matrix {:w}")
@given("the following 2x2 matrix {:w}:")
@given("the following 3x3 matrix {:w}")
@given("the following 3x3 matrix {:w}:")
@given("the following 4x4 matrix {:w}")
@given("the following 4x4 matrix {:w}:")
def step_matrix_create_empty_n_m(context, name):
    context.scenario_vars[name] = create_table_from(context)


@then("{:w}[{:d},{:d}] = {:g}")
def step_matrix_element_equals(context, name, x, y, expected):
    assert_equal(context.scenario_vars[name][x, y], expected)


@then("{:w}[{:d},{:d}] = {:rn}")
def step_matrix_element_approximately_equals(context, name, x, y, expected):
    assert_approximately_equal(context.scenario_vars[name][x, y], expected)


@then("{:l} = {:l}")
def step_matrix_equals(context, a, b):
    assert_array_equal(context.scenario_vars[a], context.scenario_vars[b])


@then("{:l} * {:l} = {:l}")
def step_matrix_tuple_multiplication_equals(context, a, b, c):
    assert_array_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), context.scenario_vars[c])


@then("{:l} * {:l} = point({:g}, {:g}, {:g})")
def step_matrix_point_multiplication_equals(context, a, b, x, y, z):
    assert_array_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), point(x, y, z))


@then("{:l} * {:l} = vector({:g}, {:g}, {:g})")
def step_matrix_vector_multiplication(context, a, b, x, y, z):
    assert_array_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), vector(x, y, z))


@then("{:l} != {:l}")
def step_matrix_not_equals(context, a, b):
    assert_array_not_equal(context.scenario_vars[a], context.scenario_vars[b])


@then("{:l} * {:l} is the following 4x4 matrix")
@then("{:l} * {:l} is the following 4x4 matrix:")
def step_matrix_multiplication_equals(context, a, b):
    assert_array_equal(matmul(context.scenario_vars[a], context.scenario_vars[b]), create_table_from(context))


@then("{:w} is the following 4x4 matrix")
@then("{:w} is the following 4x4 matrix:")
def step_matrix_create_4x4_matrix(context, a):
    assert_array_approximately_equal(context.scenario_vars[a], create_table_from(context))


@then("{:w}({:l}) is the following matrix")
@then("{:w}({:l}) is the following matrix:")
@then("{:w}({:l}) is the following 4x4 matrix")
@then("{:w}({:l}) is the following 4x4 matrix:")
def step_matrix_transpose_approximately_equal(context, operation, a):
    m = create_table_from(context)
    a_ = context.scenario_vars[a]
    if operation == 'transpose':
        assert_array_approximately_equal(transpose(a_), m)
    elif operation == 'inverse':
        assert_array_approximately_equal(inverse(a_), m)
    else:
        raise NotImplementedError(f"{operation}({a} is the following matrix: {m}")


@then("{:l} * identity_matrix = {:l}")
def step_matrix_identity_multiplication(context, a, b):
    a_ = context.scenario_vars[a]
    assert_array_equal(matmul(a_, eye(a_.shape[0])), context.scenario_vars[b])


@then("{:l} = identity_matrix")
def step_matrix_equals_identity(context, a):
    m = context.scenario_vars[a]
    assert_array_equal(m, eye(m.shape[0]))


@then("cofactor({:l}, {:d}, {:d}) = {:g}")
def step_matrix_cofactor_equals(context, a, r, c, expected):
    assert_approximately_equal(cofactor(context.scenario_vars[a], r, c), expected)


@then("determinant({:l}) = {:g}")
def step_matrix_determinant_equals(context, a, expected):
    assert_approximately_equal(det(context.scenario_vars[a]), expected)


@then("minor({:l}, {:d}, {:d}) = {:g}")
def step_matrix_minor_equals(context, a, r, c, expected):
    assert_approximately_equal(minor(context.scenario_vars[a], r, c), expected)


@then("{:l} * {:l} = tuple({:g}, {:g}, {:g}, {:g})")
def step_matrix_tuple_dot_product_equals(context, a, b, x, y, z, w):
    assert_array_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), Tuple(x, y, z, w))


@given("{:l} ← transpose(identity_matrix)")
def step_matrix_create_transpose(context, a):
    context.scenario_vars[a] = transpose(eye(4))


@then("identity_matrix * {:l} = {:l}")
def step_matrix_identity_tuple_multiplication_equals(context, a, b):
    a_ = context.scenario_vars[a]
    assert_array_equal(dot(eye(4), a_), context.scenario_vars[b])


@then("submatrix({:l}, {:d}, {:d}) is the following {}x{} matrix")
@then("submatrix({:l}, {:d}, {:d}) is the following {}x{} matrix:")
def step_matrix_submatrix_equals(context, a, m, n, _m, _n):
    assert_array_equal(submatrix(context.scenario_vars[a], m, n), create_table_from(context))


@step("{:l} ← submatrix({:l}, {:d}, {:d})")
def step_matrix_create_submatrix(context, b, a, m, n):
    context.scenario_vars[b] = submatrix(context.scenario_vars[a], m, n)


@step("{:l} is invertible")
def step_matrix_is_invertible(context, a):
    assert (invertible(context.scenario_vars[a]))


@step("{:l} is not invertible")
def step_matrix_is_not_invertible(context, a):
    assert (not invertible(context.scenario_vars[a]))


@step("{:l} ← inverse({:w})")
def step_matrix_create_inverse(context, b, a):
    context.scenario_vars[b] = inverse(context.scenario_vars[a])


@step("{:l} ← {:l} * {:l}")
def step_matrix_create_product(context, c, a, b):
    context.scenario_vars[c] = matmul(context.scenario_vars[a], context.scenario_vars[b])


@step("{:w} ← rotation_x({:rn})")
def step_matrix_create_rotation_x(context, c, radians):
    context.scenario_vars[c] = rotation_x(radians)


@then("{:l} * inverse({:l}) = {:l}")
def step_matrix_inverse_multiplication_equals(context, c, b, a):
    assert_array_approximately_equal(matmul(context.scenario_vars[c], inverse(context.scenario_vars[b])),
                                     context.scenario_vars[a])


@step("{:l} ← scaling({:g}, {:g}, {:g})")
def step_matrix_create_scaling(context, a, x, y, z):
    context.scenario_vars[a] = scaling(x, y, z)


@step("{:l} ← translation({:g}, {:g}, {:g})")
def step_matrix_create_translation(context, a, x, y, z):
    context.scenario_vars[a] = translation(x, y, z)


@then("{:l} * {:l} = point({:g}, {:g}, {:g})")
def step_matrix_translate_point_equals(context, a, b, x, y, z):
    assert_array_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), point(x, y, z))


@then("{:l}_{:l} * {:l} = point({:g}, {:rn}, {:rn})")
def step_matrix_translate_with_radicals_point_approximately_equals(context, a_0, a_1, b, x, y, z):
    assert_array_approximately_equal(dot(context.scenario_vars[f"{a_0}_{a_1}"], context.scenario_vars[b]),
                                     point(x, y, z))


@then("{:l} * {:l} = point({:g}, {:rn}, {:rn})")
def step_matrix_translate_with_radicals_alt1_point_approximately_equals(context, a, b, x, y, z):
    assert_array_approximately_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), point(x, y, z))


@then("{:l}_{:l} * {:l} = point({:g}, {:g}, {:g})")
def step_matrix_translate_point_approximately_equals(context, a_0, a_1, b, x, y, z):
    assert_array_approximately_equal(dot(context.scenario_vars[f"{a_0}_{a_1}"], context.scenario_vars[b]),
                                     point(x, y, z))


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
