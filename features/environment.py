from cmath import sqrt, pi, inf
import re

from parse import with_pattern

from color import Color
from tuple import Tuple


@with_pattern(r'(-?√?π?\d*\s*/\s*\d+)|(√\d+)')
def parse_ratio(text):
    a = text
    m = re.match("^(-)?(√)?(\d+)/(\d+)$", a)
    if m:
        groups = m.groups()
        sign = -1 if groups[0] else 1
        numerator = sqrt(int(groups[2])) if groups[1] else int(groups[2])
        denominator = int(groups[3])
        return sign * numerator / denominator
    a = text
    m = re.match(r'π / (\d+)$', a)
    if m:
        return pi / int(m.groups()[0])
    m = re.match(r'√(\d+)$', a)
    if m:
        return sqrt(int(m.groups()[0]))
    return inf


def before_feature(context, feature):
    context.scenario_vars = dict()


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
