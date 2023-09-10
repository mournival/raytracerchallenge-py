import math
from collections import namedtuple
from dataclasses import dataclass

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

    def transform(self, m):
        return ray(dot(m, self.origin), dot(m, self.direction))


ray = Ray

@dataclass
class PointLight:
    position: tuple
    intensity: color
    
    
point_light = PointLight
# point_light = namedtuple('PointLight', 'position, intensity')
material = namedtuple('Material',
                      'color ambient diffuse specular shininess',
                      defaults=(
                          color(1, 1, 1),
                          0.1,
                          0.9,
                          0.9,
                          200.0
                      ))


def lighting(m, light, pos, eye_v, normal_v):
    effective_color = m.color * light.intensity
    light_v = normalize(light.position - pos)

    ambient = effective_color * m.ambient
    light_dot_normal = dot(light_v, normal_v)
    if light_dot_normal < 0:
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
