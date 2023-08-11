import numpy as np
from behave import *
from behave.model import Row

from features.environment import assert_equal

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
    assert_array_equal(np.dot(context.globals[a], context.globals[b]), create_table_from(context))


@then("transpose({:l}) is the following matrix")
def step_impl(context, a):
    assert_array_equal(np.transpose(context.globals[a]), create_table_from(context))


def assert_array_equal(actual, expected):
    assert np.array_equal(actual, expected), f"{actual} != {expected}"


def assert_array_not_equal(actual, expected):
    assert ~np.array_equal(actual, expected), f"{actual} = {expected}"


def create_table_from(context):
    heading_row = Row(context.table.headings, context.table.headings)
    table_data = context.table.rows
    table_data.insert(0, heading_row)
    return np.array(table_data, dtype='float')
