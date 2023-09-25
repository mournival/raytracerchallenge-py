import math
from dataclasses import dataclass, field

import numpy as np

import tuple
from color import color
from matrix import dot
from tuple import normalize


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


@dataclass
class Material:
    color: np.array = field(default_factory=list)
    ambient: float = 0.1
    diffuse: float = 0.9
    specular: float = 0.9
    shininess: float = 200.0

    def __post_init__(self):
        if len(self.color) < 3:
            self.color = color(1, 1, 1)

    def set_color(self, c):
        return material(c, self.ambient, self.diffuse, self.specular, self.shininess)

    def set_diffuse(self, c):
        return material(self.color, self.ambient, c, self.specular, self.shininess)

    def set_specular(self, c):
        return material(self.color, self.ambient, self.diffuse, c, self.shininess)

    def __eq__(self, other):
        return np.allclose(self.color, other.color) and (
                self.ambient == other.ambient and self.diffuse == other.diffuse and
                self.specular == other.specular and self.shininess == other.shininess)


material = Material


def lighting(m, light, pos, eye_v, normal_v, in_shadow=False):
    effective_color = m.color * light.intensity
    light_v = normalize(light.position - pos)

    ambient = effective_color * m.ambient
    light_dot_normal = dot(light_v, normal_v)
    if light_dot_normal < 0 or in_shadow:
        diffuse = color(0, 0, 0)
        specular = color(0, 0, 0)
    else:
        diffuse = effective_color * light_dot_normal * m.diffuse

        reflect_v = tuple.reflect(-light_v, normal_v)
        reflect_dot_eye = dot(reflect_v, eye_v)

        if reflect_dot_eye <= 0:
            specular = color(0, 0, 0)
        else:
            factor = math.pow(reflect_dot_eye, m.shininess)
            specular = light.intensity * m.specular * factor

    return ambient + diffuse + specular
