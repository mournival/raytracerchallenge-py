import math
import re
from math import sqrt

import numpy
import numpy as np
from behave.model import Row
from parse import with_pattern
from parse_type import TypeBuilder

import canvas
from color import color, red, blue, green
from intersect import intersections, hit, intersection
from matrix import array_equal, array_approximately_equal, matrix, transpose, translation, scaling, minor, inverse, \
    cofactor, det, rotation_x, rotation_y, rotation_z, shearing
from ray import ray, point_light, material, lighting
from sphere import sphere
from tuple import y, vector3, vector4, point, normalize, magnitude, cross3, dot, z, w, x, is_point, reflect
from world import world, default_world


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


@with_pattern(r'-?√?\d*\s*/\s*\d+|\d+/√\d+|√\d+|π\s*/\s*\d+|-?\d+|-?\d+.\d+')
def parse_user_g(text):
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
    m = re.match(r'π\s*/\s*(\d+)$', text)
    if m:
        return math.pi / int(m.groups()[0])
    m = re.match(r'^(-?\d*)$', text)
    if m:
        return int(m.groups()[0])
    return float(text)


@with_pattern(r'[a-zA-Z]+_[a-zA-Z]+|[a-zA-Z]+|[a-z]\d')
def parse_id(text):
    return text


parse_user_g_many = TypeBuilder.with_many(parse_user_g)
parse_id_many = TypeBuilder.with_many(parse_id)

operation_mapping = {
    'canvas': canvas.Canvas,
    'cofactor': cofactor,
    'color': color,
    'cross': cross3,
    'default_world': default_world,
    'determinant': det,
    'dot': dot,
    'hit': hit,
    # 'intersect': intersect,
    'intersection': intersection,
    'intersections': intersections,
    'inverse': inverse,
    'is_point': is_point,
    'is_vector': is_point,
    'lighting': lighting,
    'magnitude': magnitude,
    'material': material,
    'material.color': lambda prop, val: material(color(*[float(c) for c in val])),
    'material.diffuse': lambda prop, val: material(diffuse=float(val)),
    'material.specular': lambda prop, val: material(specular=float(val)),
    'minor': minor,
    'normalize': normalize,
    'point': point,
    'point_light': point_light,
    'ray': ray,
    'reflect': reflect,
    'rotation_x': rotation_x,
    'rotation_y': rotation_y,
    'rotation_z': rotation_z,
    'scaling': scaling,
    'shearing': shearing,
    'sphere': sphere,
    'translation': translation,
    'transpose': transpose,
    'tuple': vector4,
    'vector': vector3,
    'world': world,
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
    '\.ambient': lambda ob: ob.ambient,
    '\.blue': blue,
    '\.count': lambda lx: len(lx),
    '\.color': lambda ob: ob.color,
    '\.direction': lambda r: r.direction,
    '\.diffuse': lambda r: r.diffuse,
    '\.green': green,
    '\.height': lambda c: c.height,
    '\.intensity': lambda r: r.intensity,
    '\.light': lambda w: w.light,
    '\.object': lambda ob: ob.object,
    '\.origin': lambda ob: ob.origin,
    '\.position': lambda ob: ob.position,
    '\.red': red,
    '\.specular': lambda o: o.specular,
    '\.shininess': lambda o: o.shininess,
    '\.t': lambda i: i.t,
    '\.transform': lambda o: o.transform,
    '\.w': w,
    '\.width': lambda c: c.width,
    '\.x': x,
    '\.y': y,
    '\.z': z,
}


@with_pattern(r"|".join(fields_mapping))
def parse_field(text):
    return fields_mapping[f"\\{text}"]


method_mapping = {
    "normal_at": lambda s, p: s.normal_at(p),
    "intersect": lambda s, p: s.intersect(p),
    "position": lambda s, p: s.position(p),
    "transform": lambda s, p: s.set_transform(p),
    "material.color": lambda s, p: s.set_color(p),
    "material.diffuse": lambda s, p: s.set_diffuse(p),
    "material.specular": lambda s, p: s.set_specular(p),
    "set_transform": lambda s, p: s.set_transform(p),

}


@with_pattern(r"|".join(method_mapping))
def parse_method(text):
    return method_mapping[text]
