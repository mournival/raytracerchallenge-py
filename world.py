from dataclasses import dataclass
from typing import List

import material as mat
from color import color
from intersect import intersections, hit, Computations
from matrix import scaling
from ray import point_light, lighting, ray
from sphere import sphere
from tuple import point, magnitude, normalize


def _flatten(a: List[List[any]]) -> List[any]:
    return [item for sublist in a for item in sublist]


@dataclass()
class World:
    light: point_light
    entities: list[sphere]

    def intersect(self, r):
        return intersections(*_flatten([o.intersect(r) for o in self.entities]))

    def is_shadowed(self, p):
        v = self.light.position - p
        direction = normalize(v)
        h = hit(self.intersect(ray(p, direction)))
        return h and h.t <= magnitude(v)


def world():
    return World(None, [])


def default_world():
    return World(
        point_light(point(-10, 10, -10), color(1, 1, 1)),
        [
            sphere(
                material=mat.material(color(0.8, 1.0, 0.6), diffuse=0.7, specular=0.2)
            ),
            sphere(
                transform_matrix=scaling(0.5, 0.5, 0.5))
        ]
    )


def color_at(w, r):
    h = hit(w.intersect(r))
    return shade_hit(w, Computations(h, r)) if h is not None else color(0, 0, 0)


def shade_hit(w, comps):
    return lighting(comps.object.material, w.light, comps.over_point, comps.eyev, comps.normalv,
                    is_shadowed(w, comps.over_point))


def is_shadowed(w: World, p):
    v = w.light.position - p
    distance = magnitude(v)
    direction = normalize(v)

    h = hit(w.intersect(ray(p, direction)))

    return h is not None and h.t < distance
