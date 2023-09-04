from collections import namedtuple

from color import color
from matrix import dot

ray = namedtuple('Ray', 'origin direction')


def position(r, t):
    return r.origin + r.direction * t


def transform(r, m):
    return ray(dot(m, r.origin), dot(m, r.direction))


point_light = namedtuple('PointLight', 'position, intensity')
material = namedtuple('Material',
                      'color ambient diffuse specular shininess',
                      defaults=(
                          color(1, 1, 1),
                          0.1,
                          0.9,
                          0.9,
                          200.0
                      ))
