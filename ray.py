import math
from dataclasses import dataclass

import numpy as np

from color import color
from matrix import dot
from tuple import normalize, reflect


@dataclass
class Ray:
    origin: tuple
    direction: tuple

    def position(self, t):
        return self.origin + self.direction * t

    def set_transform(self, m):
        return ray(dot(m, self.origin), dot(m, self.direction))


ray = Ray


@dataclass
class PointLight:
    position: tuple
    intensity: color

    def __eq__(self, other):
        return np.allclose(self.position, other.position) and np.allclose(self.intensity, other.intensity)


point_light = PointLight


def lighting(m, light, pos, eye_v, normal_v, is_shadowed=False):
    if m.pattern is not None:
        effective_color = m.pattern.color_at(pos) * light.intensity
    else:
        effective_color = m.color * light.intensity
    light_v = normalize(light.position - pos)

    ambient = effective_color * m.ambient

    light_dot_normal = dot(light_v, normal_v)
    if light_dot_normal < 0 or is_shadowed:
        diffuse = color(0, 0, 0)
        specular = color(0, 0, 0)
    else:
        diffuse = effective_color * light_dot_normal * m.diffuse

        reflect_v = reflect(-light_v, normal_v)
        reflect_dot_eye = dot(reflect_v, eye_v)

        if reflect_dot_eye <= 0:
            specular = color(0, 0, 0)
        else:
            factor = math.pow(reflect_dot_eye, m.shininess)
            specular = light.intensity * m.specular * factor

    return ambient + diffuse + specular
