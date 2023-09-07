from dataclasses import dataclass

from color import color
from matrix import scaling
from ray import point_light, material
from sphere import sphere
from tuple import point


@dataclass()
class World:
    light: point_light
    entities: list[sphere]


def world():
    return World(None, [])


default_world = World(
    point_light(point(-10, 10, -10), color(1, 1, 1)),
    [
        sphere(
            material=material(color(0.8, 1.0, 0.6), diffuse=0.7, specular=0.2)
        ),
        sphere(
            transform_matrix=scaling(0.5, 0.5, 0.5))
    ]
)
