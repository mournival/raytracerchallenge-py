from behave import *
from behave.model import Row

from features.environment import assert_equal, assert_approximately_equal
from matrix import eye, det, matrix, transpose, matmul, array_equal, dot
from tuple import Tuple

use_step_matcher("parse")


@given("the following {:d}x{:d} matrix {:w}")
def step_impl(context, m, n, name):
    context.globals[name] = create_table_from(context)


@given("the following matrix {:w}")
def step_impl(context, name):
    context.globals[name] = create_table_from(context)


@then("{:w}[{:d},{:d}] = {:g}")
def step_impl(context, name, x, y, expected):
    assert_equal(context.globals[name][x, y], expected)


@then("{:l} = {:l}")
def step_impl(context, a, b):
    assert_array_equal(context.globals[a], context.globals[b])


@then("{:l} != {:l}")
def step_impl(context, a, b):
    assert_array_not_equal(context.globals[a], context.globals[b])


@then("{:l} * {:l} is the following 4x4 matrix")
def step_impl(context, a, b):
    assert_array_equal(matmul(context.globals[a], context.globals[b]), create_table_from(context))


@then("{:l} * identity_matrix = {:l}")
def step_impl(context, a, b):
    A = context.globals[a]
    assert_array_equal(matmul(A, eye(A.shape[0])), context.globals[b])


@then("{:l} = identity_matrix")
def step_impl(context, a):
    A = context.globals[a]
    assert_array_equal(A, eye(A.shape[0]))


@then("transpose({:l}) is the following matrix")
def step_impl(context, a):
    assert_array_equal(transpose(context.globals[a]), create_table_from(context))


@then("determinant({:l}) = {:g}")
def step_impl(context, a, expected):
    assert_approximately_equal(det(context.globals[a]), expected)


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


def assert_array_equal(actual, expected):
    assert array_equal(actual, expected), f"{actual} != {expected}"


def assert_array_not_equal(actual, expected):
    assert ~array_equal(actual, expected), f"{actual} = {expected}"


def create_table_from(context):
    heading_row = Row(context.table.headings, context.table.headings)
    table_data = context.table.rows
    table_data.insert(0, heading_row)
    return matrix(table_data)
