import math

import numpy as np

import material as mat
import tuple as tp
from intersect import intersection
from matrix import eye, dot
from ray import ray
from shape import Shape


class TestShape(Shape):
    def __init__(self, transform_matrix=eye(4), material: mat.material = mat.Material()):
        super().__init__(transform_matrix, material)
        self.saved_ray = None

    def local_intersect(self, r: ray):
        self.saved_ray = r
        sphere_to_ray = r.origin - tp.point(0, 0, 0)
        a = tp.dot(r.direction, r.direction)
        b = 2 * tp.dot(r.direction, sphere_to_ray)
        c = tp.dot(sphere_to_ray, sphere_to_ray) - 1
        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return []
        d = math.sqrt(discriminant)
        return [intersection((-b - d) / (2 * a), self), intersection((-b + d) / (2 * a), self)]

    def local_normal_at(self, world_point):
        object_point = dot(self._inverse_transform, world_point)
        return object_point - tp.point(0, 0, 0)

    def set_transform(self, t) -> np.array:
        return TestShape(t, self.material)

    def set_material(self, m):
        return TestShape(self.transform, m)