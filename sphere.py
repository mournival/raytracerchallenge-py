import math

import numpy as np

import matrix
import tuple as tp
from intersect import intersection
from matrix import inverse, eye
from ray import ray, material


class Sphere(object):

    def __init__(self, transform_matrix=eye(4), material=material()):
        self.transform = transform_matrix
        self._inverse_transform = inverse(self.transform)
        self.material = material

    def intersect(self, r: ray):
        tray = r.set_transform(self._inverse_transform)
        sphere_to_ray = tray.origin - tp.point(0, 0, 0)
        a = tp.dot(tray.direction, tray.direction)
        b = 2 * tp.dot(tray.direction, sphere_to_ray)
        c = tp.dot(sphere_to_ray, sphere_to_ray) - 1
        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return []
        d = math.sqrt(discriminant)
        return [intersection((-b - d) / (2 * a), self), intersection((-b + d) / (2 * a), self)]

    def normal_at(self, world_point):
        object_point = matrix.dot(self._inverse_transform, world_point)
        object_normal = object_point - tp.point(0, 0, 0)
        world_normal = matrix.dot(matrix.transpose(self._inverse_transform), object_normal)
        return tp.normalize(tp.vector3(tp.x(world_normal), tp.y(world_normal), tp.z(world_normal)))

    def set_transform(self, t):
        return sphere(t)
    
    def __eq__(self, other):
        return self.material == other.material and np.allclose(self.transform, other.transform)


sphere = Sphere
