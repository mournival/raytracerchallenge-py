from dataclasses import dataclass
from typing import List

import numpy as np

from ray import Ray
from tuple import dot

EPSILON = 0.00001


@dataclass
class Intersection:
    t: float
    object: any

    def intersect(self, r):
        return self.object.intersect(r)


class Computations:
    t: float
    object: any
    point: np.array
    eyev: np.array
    normalv: np.array
    inside: bool

    def __init__(self, i: Intersection, r: Ray):
        self.t = i.t
        self.object = i.object
        self.point = r.position(i.t)
        self.eyev = -r.direction
        self.normalv = i.object.normal_at(self.point)
        self.inside = dot(self.normalv, self.eyev) < 0
        if self.inside:
            self.normalv = -self.normalv
        self.over_point = self.point + self.normalv * EPSILON


intersection = Intersection


def intersections(*t1):
    return [i for i in sorted(t1, key=lambda i: i.t)]


def hit(xs: List[intersection]):
    return next((x for x in xs if x.t >= 0), None)
