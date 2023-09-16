from dataclasses import dataclass
from typing import List

from color import color
from intersect import intersections
from matrix import scaling
from ray import point_light, material, lighting
from sphere import sphere
from tuple import point


def _flatten(a: List[List[any]]) -> List[any]:
    return [item for sublist in a for item in sublist]


@dataclass()
class World:
    light: point_light
    entities: list[sphere]

    def intersect(self, r):
        return intersections(*_flatten([o.intersect(r) for o in self.entities]))


def world():
    return World(None, [])


def default_world():
    return World(
        point_light(point(-10, 10, -10), color(1, 1, 1)),
        [
            sphere(
                material=material(color(0.8, 1.0, 0.6), diffuse=0.7, specular=0.2)
            ),
            sphere(
                transform_matrix=scaling(0.5, 0.5, 0.5))
        ]
    )


def color_at(w, c):
    return None


def shade_hit(w, comps):
    return lighting(comps.object.material, w.light, comps.point, comps.eyev, comps.normalv)