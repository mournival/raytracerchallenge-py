from behave import *
from behave.model import Row

from features.environment import assert_equal, assert_approximately_equal
from matrix import eye, det, matrix, transpose, matmul, array_equal, dot, submatrix, minor, cofactor, invertible, \
    inverse, array_approximately_equal
from tuple import Tuple

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
def step_impl(context, name, x, y, numerator, denomator):
    assert_approximately_equal(context.globals[name][x, y], numerator / denomator)


@then("{:l} = {:l}")
def step_impl(context, a, b):
    assert_array_equal(context.globals[a], context.globals[b])


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


@step("{:l} ← inverse({:l})")
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


def assert_array_equal(actual, expected):
    assert array_equal(actual, expected), f"{actual} != {expected}"


def assert_array_approximately_equal(actual, expected):
    assert array_approximately_equal(actual, expected), f"{actual} != {expected}"


def assert_array_not_equal(actual, expected):
    assert not array_equal(actual, expected), f"{actual} = {expected}"


@step("{:l} ← {:l} * {:l}")
def step_impl(context, c, a, b):
    context.globals[c] = matmul(context.globals[a], context.globals[b])
