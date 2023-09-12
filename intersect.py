from dataclasses import dataclass
from typing import List

import numpy as np

from ray import Ray


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

    def __init__(self, i: Intersection, r: Ray):
        self.t = i.t
        self.object = i.object
        self.point = r.position(i.t)
        self.eyev = -r.direction
        self.normalv = i.object.normal_at(self.point)


intersection = Intersection


def intersections(*t1):
    return [i for i in sorted(t1, key=lambda i: i.t)]


def hit(xs: List[intersection]):
    return next((x for x in xs if x.t >= 0), None)
