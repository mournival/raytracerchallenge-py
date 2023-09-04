import math
import re
from math import sqrt

import numpy
import numpy as np
from behave.model import Row
from parse import with_pattern

import canvas
from color import color, red, blue, green
from intersect import intersections, hit, intersection, intersect
from matrix import array_equal, array_approximately_equal, matrix, transpose, translation, scaling, minor, inverse, \
    cofactor, det, rotation_x, rotation_y, rotation_z
from ray import transform, ray, position
from tuple import y, vector, tuple_trtc, point, normalize, magnitude, cross, dot, z, w, x, is_point


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
    m = re.match(r'π / (\d+)$', text)
    if m:
        return math.pi / int(m.groups()[0])
    raise ValueError()


@with_pattern(r'[a-zA-Z]+_[a-zA-Z]+|[a-zA-Z]+|[aicprv]\d')
def parse_id(text):
    return text


operation_mapping = {
    'canvas': canvas.Canvas,
    'cofactor': cofactor,
    'color': color,
    'cross': cross,
    'determinant': det,
    'dot': dot,
    'hit': hit,
    'intersect': intersect,
    'intersection': intersection,
    'intersections': intersections,
    'inverse': inverse,
    'is_point': is_point,
    'is_vector': is_point,
    'magnitude': magnitude,
    'minor': minor,
    'normalize': normalize,
    'point': point,
    'position': position,
    'ray': ray,
    'rotation_x': rotation_x,
    'rotation_y': rotation_y,
    'rotation_z': rotation_z,
    'scaling': scaling,
    'transform': transform,
    'translation': translation,
    'transpose': transpose,
    'tuple': tuple_trtc,
    'vector': vector,
}


@with_pattern(r"|".join(operation_mapping))
def parse_operation(text):
    return operation_mapping[text]


@with_pattern(r'the following (\dx\d )?matrix \w+:?')
def parse_matrix_name(text):
    m = re.match(r'the following \d?x?\d? ?matrix (\w):?', text)
    return m.groups()[0]


is_is_not_mapping = {'is a': True,
                     'is not a': False}


@with_pattern(r"|".join(is_is_not_mapping))
def parse_is_is_not(text):
    return is_is_not_mapping[text]


fields_mapping = {
    '.blue': blue,
    '.count': lambda lx: len(lx),
    '.direction': lambda r: r.direction,
    '.green': green,
    '.height': lambda c: c.height,
    '.object': lambda ob: ob.object,
    '.origin': lambda ob: ob.origin,
    '.red': red,
    '.t': lambda i: i.t,
    '.transform': lambda o: o.transform,
    '.w': w,
    '.width': lambda c: c.width,
    '.x': x,
    '.y': y,
    '.z': z,
}


@with_pattern(r"|".join(fields_mapping))
def parse_field(text):
    return fields_mapping[text]


methods_mapping = {
    "normal_at": lambda s, p: s.normal_at(p)
}


@with_pattern(r"|".join(methods_mapping))
def parse_method(text):
    return methods_mapping[text]
