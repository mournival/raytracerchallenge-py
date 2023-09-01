import math
import re
from math import sqrt

import numpy
import numpy as np
from behave.model import Row
from parse import with_pattern

from color import color, red, blue, green
from intersect import intersections, hit, intersection, intersect
from matrix import array_equal, array_approximately_equal, matrix, transpose, translation, scaling, minor, inverse, \
    cofactor, det
from ray import transform, ray, position
from tuple import o, y, z, w, vector, tuple_trtc, point, normalize, magnitude, cross, dot


def before_feature(context, _feature):
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


@with_pattern(r'[a-zA-Z]+_[a-zA-Z]+|[a-zA-Z]+|[aicprv]\d')
def parse_id(text):
    return text


@with_pattern(r'\w+')
def parse_operation(text):
    if text == 'blue':
        return blue
    if text == 'cofactor':
        return cofactor
    if text == 'color':
        return color
    if text == 'cross':
        return cross
    if text == 'determinant':
        return det
    if text == 'direction':
        return lambda r: r.direction
    if text == 'dot':
        return dot
    if text == 'green':
        return green
    if text == 'hit':
        return hit
    if text == 'intersect':
        return intersect
    if text == 'intersection':
        return intersection
    if text == 'intersections':
        return intersections
    if text == 'inverse':
        return inverse
    if text == 'magnitude':
        return magnitude
    if text == 'minor':
        return minor
    if text == 'normalize':
        return normalize
    if text == 'object':
        return lambda ob: ob.object
    if text == 'origin':
        return lambda r: r.origin
    if text == 'point':
        return point    
    if text == 'position':
        return position
    if text == 'ray':
        return ray
    if text == 'red':
        return red
    if text == 'scaling':
        return scaling
    if text == 't':
        return lambda i: i.t
    if text == 'transform':
        return transform
    if text == 'translation':
        return translation
    if text == 'transpose':
        return transpose
    if text == 'tuple':
        return tuple_trtc
    if text == 'vector':
        return vector
    if text == 'w':
        return w
    if text == 'x':
        return o
    if text == 'y':
        return y
    if text == 'z':
        return z
    raise ValueError()


@with_pattern(r'the following (\dx\d )?matrix \w+:?')
def parse_matrix_name(text):
    m = re.match(r'the following \d?x?\d? ?matrix (\w):?', text)
    return m.groups()[0]


is_is_not_mapping = {'is a': True,
                     'is not a': False}


@with_pattern(r"|".join(is_is_not_mapping))
def parse_is_is_not(text):
    return is_is_not_mapping[text.lower()]
