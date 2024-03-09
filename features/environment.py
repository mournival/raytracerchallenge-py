import math
import re
from math import sqrt

import numpy
import numpy as np
from behave.model import Row
from parse import with_pattern
from parse_type import TypeBuilder

import camera
import canvas
import material as mat
from color import color
from intersect import intersections, hit, Computations
from matrix import array_equal, array_approximately_equal, matrix, transpose, translation, scaling, minor, inverse, \
    cofactor, det, rotation_x, rotation_y, rotation_z, shearing, view_transform
from ray import ray, point_light, lighting
from sphere import sphere
from test_shape import TestShape
from tuple import vector3, vector4, point, normalize, magnitude, cross3, dot, is_point, reflect
from world import world, default_world, color_at, shade_hit


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


number_patterns = [
    '√\d+',
    '\d*/√\d+',
    '-√\d*\s*/\s*\d+',
    '√\d*\s*/\s*\d+',
    '-\d*\s*/\s*\d+',
    '\d*\s*/\s*\d+',
    'π\s*/\s*\d+',
    '-?\d+',
    '-?\d+\.\d+'
]


@with_pattern(r"|".join(number_patterns))
def parse_user_g(text):
    m = re.match(r'^√(\d+)$', text)
    if m:
        return sqrt(int(m.groups()[0]))
    m = re.match('^(\d*)/√(\d+)$', text)
    if m:
        g = m.groups()
        return int(g[0]) / sqrt(int(g[1]))
    m = re.match('^-√(\d*)\s*/\s*(\d+)$', text)
    if m:
        g = m.groups()
        return -sqrt(int(g[0])) / int(g[1])
    m = re.match(r'^√(\d*)\s*/\s*(\d+)$', text)
    if m:
        g = m.groups()
        return sqrt(int(g[0])) / int(g[1])
    m = re.match('^-(\d*)\s*/\s*(\d+)$', text)
    if m:
        g = m.groups()
        return -int(g[0]) / int(g[1])
    m = re.match(r'^(\d*)\s*/\s*(\d+)$', text)
    if m:
        g = m.groups()
        return int(g[0]) / int(g[1])
    m = re.match(r'^π\s*/\s*(\d+)$', text)
    if m:
        return math.pi / int(m.groups()[0])
    m = re.match(r'^(-?\d+)$', text)
    if m:
        return int(m.groups()[0])
    return float(text)


id_patterns = [
    '[a-zA-Z]+_[a-zA-Z]+',
    '[a-zA-Z]+_[a-zA-Z]+_[a-zA-Z]+',
    '[a-zA-Z]{1,3}',
    '(?!true)[a-zA-Z]{4}',
    '(?!false)[a-zA-Z]{5}',
    '[a-zA-Z]{1,3}|[a-zA-Z]{6,}',
    '[a-z]\d'
]


@with_pattern(r"|".join(id_patterns))
def parse_id(text):
    return text


parse_user_g_many = TypeBuilder.with_many(parse_user_g)
parse_id_many = TypeBuilder.with_many(parse_id)

operation_mapping = {
    'camera': camera.Camera,
    'canvas': canvas.Canvas,
    'cofactor': cofactor,
    'color': color,
    'color_at': color_at,
    'cross': cross3,
    'default_world': default_world,
    'determinant': det,
    'dot': dot,
    'hit': hit,
    'intersections': intersections,
    'inverse': inverse,
    'is_point': is_point,
    'is_vector': is_point,
    'lighting': lighting,
    'magnitude': magnitude,
    'material': mat.material,
    'material.color': lambda prop, val: mat.material(color(*[float(c) for c in val])),
    'material.diffuse': lambda prop, val: mat.material(diffuse=float(val)),
    'material.specular': lambda prop, val: mat.material(specular=float(val)),
    'minor': minor,
    'normalize': normalize,
    'point': point,
    'point_light': point_light,
    'prepare_computations': Computations,
    'ray': ray,
    'ray_for_pixel': camera.ray_for_pixel,
    'reflect': reflect,
    'rotation_x': rotation_x,
    'rotation_y': rotation_y,
    'rotation_z': rotation_z,
    'scaling': scaling,
    'shade_hit': shade_hit,
    'shearing': shearing,
    'sphere': sphere,
    'test_shape': TestShape,
    'translation': translation,
    'transpose': transpose,
    'tuple': vector4,
    'vector': vector3,
    'view_transform': view_transform,
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
    '\.count': lambda lx: len(lx),
    '\.color': lambda ob: ob.color,
    '\.direction': lambda r: r.direction,
    '\.diffuse': lambda r: r.diffuse,
    '\.eyev': lambda r: r.eyev,
    '\.field_of_view': lambda c: c.field_of_view,
    '\.height': lambda c: c.height,
    '\.inside': lambda i: i.inside,
    '\.intensity': lambda r: r.intensity,
    '\.light': lambda o: o.light,
    '\.material': lambda o: o.material,
    '\.normalv': lambda o: o.normalv,
    '\.object': lambda o: o.object,
    '\.origin': lambda o: o.origin,
    '\.pixel_size': lambda o: o.pixel_size,
    '\.point': lambda o: o.point,
    '\.position': lambda o: o.position,
    '\.specular': lambda o: o.specular,
    '\.shininess': lambda o: o.shininess,
    '\.t': lambda i: i.t,
    '\.transform': lambda o: o.transform,
    '\.width': lambda c: c.width,
}


@with_pattern(r"|".join(fields_mapping))
def parse_field(text):
    return fields_mapping[f"\\{text}"]


method_mapping = {
    "intersect_world": lambda s, p: s.intersect(p),
    "is_shadowed": lambda s, p: s.is_shadowed(p),
    "position": lambda s, p: s.position(p),
    "transform": lambda s, p: s.set_transform(p),
    "material.set_ambient": lambda s, p: s.set_ambient(p),
    "material.color": lambda s, p: s.set_color(p),
    "material.diffuse": lambda s, p: s.set_diffuse(p),
    "material.specular": lambda s, p: s.set_specular(p),
    "render": lambda s, wld: s.render(wld),
    "set_ambient": lambda s, p: s.set_ambient(p),
    "set_color": lambda s, p: s.set_color(p),
    "set_transform": lambda s, p: s.set_transform(p),
}


@with_pattern(r"|".join(method_mapping))
def parse_method(text):
    return method_mapping[text]
