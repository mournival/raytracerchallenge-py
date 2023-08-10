from color import Color
from tuple import Tuple


def before_feature(context, feature):
    context.tuples = dict()
    context.globals = dict()


def assert_equal(actual, expected):
    assert actual == expected, f"{actual} != {expected}"


def assert_approximately_equal(actual, expected):
    epsilon = 0.0001
    assert abs((actual - expected)) < epsilon, f"{actual} !~ {expected}"


def assert_approximate_xyz(actual: Tuple, x, y, z):
    assert_approximately_equal(actual.x, x)
    assert_approximately_equal(actual.y, y)
    assert_approximately_equal(actual.z, z)


def assert_approximate_rgb(actual: Color, red, green, blue):
    assert_approximately_equal(actual.red, red)
    assert_approximately_equal(actual.green, green)
    assert_approximately_equal(actual.blue, blue)
