from cmath import pi, sqrt

from behave import *
from behave.model import Row

from features.environment import assert_equal, assert_approximately_equal
from matrix import eye, det, matrix, transpose, matmul, array_equal, dot, submatrix, minor, cofactor, invertible, \
    inverse, array_approximately_equal, scaling, translation, rotation_x
from tuple import Tuple, point, vector

use_step_matcher("parse")


@given("the following {:d}x{:d} matrix {:w}")
@given("the following {:d}x{:d} matrix {:w}:")
def step_impl(context, m, n, name):
    context.globals[name] = create_table_from(context)


@given("the following matrix {:w}")
@given("the following matrix {:w}:")
def step_impl(context, name):
    context.globals[name] = create_table_from(context)


@then("{:w}[{:d},{:d}] = {:g}")
def step_impl(context, name, x, y, expected):
    assert_equal(context.globals[name][x, y], expected)


@then("{:w}[{:d},{:d}] = {:d}/{:d}")
def step_impl(context, name, x, y, numerator, denominator):
    assert_approximately_equal(context.globals[name][x, y], numerator / denominator)


@then("{:l} = {:l}")
def step_impl(context, a, b):
    assert_array_equal(context.globals[a], context.globals[b])


@then("{:l} * {:l} = {:l}")
def step_impl(context, a, b, c):
    assert_array_equal(dot(context.globals[a], context.tuples[b]), context.tuples[c])


@then("{:l} * {:l} = point({:g}, {:g}, {:g})")
def step_impl(context, a, b, x, y, z):
    assert_array_equal(dot(context.globals[a], context.tuples[b]), point(x, y, z))


@then("{:l} * {:l} = vector({:g}, {:g}, {:g})")
def step_impl(context, a, b, x, y, z):
    assert_array_equal(dot(context.globals[a], context.tuples[b]), vector(x, y, z))


@then("{:l} != {:l}")
def step_impl(context, a, b):
    assert_array_not_equal(context.globals[a], context.globals[b])


@then("{:l} * {:l} is the following 4x4 matrix")
@then("{:l} * {:l} is the following 4x4 matrix:")
def step_impl(context, a, b):
    assert_array_equal(matmul(context.globals[a], context.globals[b]), create_table_from(context))


@then("{:l} * identity_matrix = {:l}")
def step_impl(context, a, b):
    a_ = context.globals[a]
    assert_array_equal(matmul(a_, eye(a_.shape[0])), context.globals[b])


@then("{:l} = identity_matrix")
def step_impl(context, a):
    m = context.globals[a]
    assert_array_equal(m, eye(m.shape[0]))


@then("transpose({:l}) is the following matrix")
@then("transpose({:l}) is the following matrix:")
def step_impl(context, a):
    assert_array_equal(transpose(context.globals[a]), create_table_from(context))


@then("cofactor({:l}, {:d}, {:d}) = {:g}")
def step_impl(context, a, r, c, expected):
    assert_approximately_equal(cofactor(context.globals[a], r, c), expected)


@then("determinant({:l}) = {:g}")
def step_impl(context, a, expected):
    assert_approximately_equal(det(context.globals[a]), expected)


@then("minor({:l}, {:d}, {:d}) = {:g}")
def step_impl(context, a, r, c, expected):
    assert_approximately_equal(minor(context.globals[a], r, c), expected)


@then("{:l} * {:l} = tuple({:g}, {:g}, {:g}, {:g})")
def step_impl(context, a, b, x, y, z, w):
    actual = dot(context.globals[a], context.tuples[b])
    assert_array_equal(actual, Tuple(x, y, z, w))


@given("{:l} ← transpose(identity_matrix)")
def step_impl(context, a):
    context.globals[a] = transpose(eye(4))


@then("identity_matrix * {:l} = {:l}")
def step_impl(context, a, b):
    a_ = context.tuples[a]
    assert_array_equal(dot(eye(4), a_), context.tuples[b])


def create_table_from(context):
    heading_row = Row(context.table.headings, context.table.headings)
    table_data = context.table.rows
    table_data.insert(0, heading_row)
    return matrix(table_data)


@then("submatrix({:l}, {:d}, {:d}) is the following {}x{} matrix")
@then("submatrix({:l}, {:d}, {:d}) is the following {}x{} matrix:")
def step_impl(context, a, m, n, _m, _n):
    assert_array_equal(submatrix(context.globals[a], m, n), create_table_from(context))


@step("{:l} ← submatrix({:l}, {:d}, {:d})")
def step_impl(context, b, a, m, n):
    context.globals[b] = submatrix(context.globals[a], m, n)


@step("{:l} is invertible")
def step_impl(context, a):
    assert (invertible(context.globals[a]))


@step("{:l} is not invertible")
def step_impl(context, a):
    assert (not invertible(context.globals[a]))


@step("{:l} ← inverse({:w})")
def step_impl(context, b, a):
    context.globals[b] = inverse(context.globals[a])


@then("{:l} is the following 4x4 matrix")
@then("{:l} is the following 4x4 matrix:")
def step_impl(context, a):
    assert_array_approximately_equal(context.globals[a], create_table_from(context))


@then("inverse({:l}) is the following 4x4 matrix")
@then("inverse({:l}) is the following 4x4 matrix:")
def step_impl(context, a):
    assert_array_approximately_equal(inverse(context.globals[a]), create_table_from(context))


@step("{:l} ← {:l} * {:l}")
def step_impl(context, c, a, b):
    context.globals[c] = matmul(context.globals[a], context.globals[b])


@step("{:w} ← rotation_x(π / {:d})")
def step_impl(context, c, denominator):
    context.globals[c] = rotation_x(pi / denominator)


@then("{:l} * inverse({:l}) = {:l}")
def step_impl(context, c, b, a):
    assert_array_approximately_equal(matmul(context.globals[c], inverse(context.globals[b])), context.globals[a])


@step("{:l} ← scaling({:g}, {:g}, {:g})")
def step_impl(context, a, x, y, z):
    context.globals[a] = scaling(x, y, z)


@step("{:l} ← translation({:g}, {:g}, {:g})")
def step_impl(context, a, x, y, z):
    context.globals[a] = translation(x, y, z)


@step("{:l} ← {:l} * {:l}")
def step_impl(context, c, a, b):
    context.globals[c] = matmul(context.globals[a], context.globals[b])


@then("{:l} * {:l} = point({:g}, {:g}, {:g})")
def step_impl(context, a, b, x, y, z):
    assert_array_equal(dot(context.globals[a], context.tuples[b]), point(x, y, z))


@then("{:l}_{:l} * {:l} = point({:g}, √{:d}/{:d}, √{:d}/{:d})")
def step_impl(context, a_0, a_1, b, x, y_n, y_d, z_n, z_d):
    assert_array_equal(dot(context.globals[f"{a_0}_{a_1}"], context.tuples[b]),
                       point(x, sqrt(y_n) / y_d, sqrt(z_n) / z_d))


@then("{:l} * {:l} = point({:g}, √{:d}/{:d}, -√{:d}/{:d})")
def step_impl(context, a, b, x, y_n, y_d, z_n, z_d):
    assert_array_approximately_equal(dot(context.globals[a], context.tuples[b]),
                       point(x, sqrt(y_n) / y_d, -sqrt(z_n) / z_d))


@then("{:l}_{:l} * {:l} = point({:g}, {:g}, {:g})")
def step_impl(context, a_0, a_1, b, x, y, z):
    assert_array_approximately_equal(dot(context.globals[f"{a_0}_{a_1}"], context.tuples[b]), point(x, y, z))


def assert_array_equal(actual, expected):
    assert array_equal(actual, expected), f"{actual} != {expected}"


def assert_array_approximately_equal(actual, expected):
    assert array_approximately_equal(actual, expected), f"{actual} != {expected}"


def assert_array_not_equal(actual, expected):
    assert not array_equal(actual, expected), f"{actual} = {expected}"
