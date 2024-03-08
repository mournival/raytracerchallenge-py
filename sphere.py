import math

import material as mat
import tuple as tp
from intersect import intersection
from matrix import eye
from ray import ray
from shape import Shape


class Sphere(Shape):

    def __init__(self, transform_matrix=eye(4), material=mat.material()):
        super().__init__(transform_matrix, material)

    def local_intersect(self, r: ray):
        sphere_to_ray = r.origin - tp.point(0, 0, 0)
        a = tp.dot(r.direction, r.direction)
        b = 2 * tp.dot(r.direction, sphere_to_ray)
        c = tp.dot(sphere_to_ray, sphere_to_ray) - 1
        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return []
        d = math.sqrt(discriminant)
        return [intersection((-b - d) / (2 * a), self), intersection((-b + d) / (2 * a), self)]

    def set_transform(self, t):
        return sphere(t, self.material)

    def set_material(self, m):
        return sphere(self.transform, m)


sphere = Sphere
