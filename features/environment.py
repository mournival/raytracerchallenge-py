from behave.model import Row

from color import Color
from matrix import matrix, array_equal
from tuple import Tuple


def before_feature(context, feature):
    context.tuples = dict()
    context.globals = dict()


def assert_approximately_equal(actual, expected):
    epsilon = 0.0001
    assert abs((actual - expected)) < epsilon, f"{actual} !~ {expected}"


def assert_approximate_rgb(actual: Color, red, green, blue):
    assert_approximately_equal(actual.red, red)
    assert_approximately_equal(actual.green, green)
    assert_approximately_equal(actual.blue, blue)


def assert_approximate_xyz(actual: Tuple, x, y, z):
    assert_approximately_equal(actual.x, x)
    assert_approximately_equal(actual.y, y)
    assert_approximately_equal(actual.z, z)


def assert_array_equal(actual, expected):
    assert array_equal(actual, expected), f"{actual} != {expected}"


def assert_array_not_equal(actual, expected):
    assert ~array_equal(actual, expected), f"{actual} = {expected}"


def create_matrix_from(context):
    heading_row = Row(context.table.headings, context.table.headings)
    table_data = context.table.rows
    table_data.insert(0, heading_row)
    return matrix(table_data)


def assert_equal(actual, expected):
    assert actual == expected, f"{actual} != {expected}"
