import numpy as np
from behave import *
from behave.model import Row

from features.environment import assert_equal

use_step_matcher("parse")


@given("the following {:d}x{:d} matrix {:w}")
def step_impl(context, m , n, name):
    heading_row = Row(context.table.headings, context.table.headings)
    table_data = context.table.rows
    table_data.insert(0, heading_row)
    context.globals[name] = np.array(table_data, dtype='float')

@given("the following matrix {:w}")
def step_impl(context, name):
    heading_row = Row(context.table.headings, context.table.headings)
    table_data = context.table.rows
    table_data.insert(0, heading_row)
    context.globals[name] = np.array(table_data, dtype='float')

@then("{:w}[{:d},{:d}] = {:g}")
def step_impl(context, name, x, y, expected):
    assert_equal(context.globals[name][x, y], expected)


@then("{:l} = {:l}")
def step_impl(context, a, b):
    assert_array_equal(context.globals[a], context.globals[b])

def assert_array_equal(actual, expected):
        assert np.array_equal(actual, expected), f"{actual} != {expected}"