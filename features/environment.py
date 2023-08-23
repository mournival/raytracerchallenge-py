import math
import re
from math import sqrt

import numpy
import numpy as np
from behave.model import Row
from parse import with_pattern

from color import color
from matrix import array_equal, array_approximately_equal, matrix


def before_feature(context, feature):
    context.scenario_vars = dict()
    context.scenario_vars['identity_matrix'] = np.eye(4)


def assert_equal(actual, expected):
    if type(actual) == numpy.ndarray:
        assert np.allclose(actual, expected), f"{actual} != {expected}"
    else:
        assert actual == expected, f"{actual} != {expected}"


def assert_approximately_equal(actual, expected):
    assert np.allclose(actual, expected, rtol=0.0001), f"{actual} != {expected}"


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


@with_pattern(r'-?√?\d*\s*/\s*\d+|\d+/√\d+|√\d+|\d+')
def parse_ratio(text):
    m = re.match(r'^√(\d+)$', text)
    if m:
        return sqrt(int(m.groups()[0]))
    m = re.match('-(\d*)\s*/√\s*(\d+)', text)
    if m:
        g = m.groups()
        return -int(g[0]) / sqrt(int(g[1]))
    m = re.match('(\d*)/√(\d+)', text)
    if m:
        g = m.groups()
        return int(g[0]) / sqrt(int(g[1]))
    m = re.match('-√(\d*)\s*/\s*(\d+)', text)
    if m:
        g = m.groups()
        return -sqrt(int(g[0])) / int(g[1])
    m = re.match(r'√(\d*)\s*/\s*(\d+)', text)
    if m:
        g = m.groups()
        return sqrt(int(g[0])) / int(g[1])
    m = re.match('-(\d*)\s*/\s*(\d+)', text)
    if m:
        g = m.groups()
        return -int(g[0]) / int(g[1])
    m = re.match(r'(\d*)\s*/\s*(\d+)', text)
    if m:
        g = m.groups()
        return int(g[0]) / int(g[1])
    m = re.match(r'^(\d*)$', text)
    if m:
        return int(m.groups()[0])
    raise ValueError()


@with_pattern(r'π\s/\s\d+')
def parse_radians(text):
    a = text
    m = re.match(r'π / (\d+)$', a)
    if m:
        return math.pi / int(m.groups()[0])
    raise ValueError()


@with_pattern(r'[a-zA-Z]+_[a-zA-Z]+|[a-zA-Z]+|[acpv]\d')
def parse_id(text):
    return text


@with_pattern(r'\w+')
def parse_operation(text):
    if text == 'blue':
        from color import blue
        return blue
    if text == 'cofactor':
        import matrix
        return matrix.cofactor
    if text == 'color':
        return color
    if text == 'cross':
        from tuple import cross
        return cross
    if text == 'determinant':
        import matrix
        return matrix.det
    if text == 'dot':
        from tuple import dot
        return dot
    if text == 'green':
        from color import green
        return green
    if text == 'inverse':
        import matrix
        return matrix.inverse
    if text == 'magnitude':
        from tuple import magnitude
        return magnitude
    if text == 'minor':
        import matrix
        return matrix.minor
    if text == 'normalize':
        from tuple import normalize
        return normalize
    if text == 'point':
        from tuple import point
        return point
    if text == 'red':
        from color import red
        return red
    if text == 'scaling':
        import matrix
        return matrix.scaling
    if text == 'translation':
        import matrix
        return matrix.translation
    if text == 'transpose':
        import matrix
        return matrix.transpose
    if text == 'vector':
        from tuple import vector
        return vector
    if text == 'w':
        from tuple import w
        return w
    if text == 'x':
        from tuple import x
        return x
    if text == 'y':
        from tuple import y
        return y
    if text == 'z':
        from tuple import z
        return z
    raise ValueError()


@with_pattern(r'the following (\dx\d )?matrix \w+:?')
def parse_matrix_name(text):
    m = re.match(r'the following \d?x?\d? ?matrix (\w):?', text)
    return m.groups()[0]
