from abc import ABC, abstractmethod

import numpy as np

import material as mat
import tuple as tp
from matrix import eye, inverse, dot, transpose
from ray import ray


class Shape(ABC):
    transform: np.array
    material: mat.Material

    # parent: Shape  # Not sure how to forward declare ...
    def __init__(self, transform_matrix=eye(4), material: mat.material = mat.Material()):
        self.transform = transform_matrix
        self.material = material
        self._inverse_transform = inverse(self.transform)
        self.parent = None

    def intersect(self, r: ray):
        local_ray = r.set_transform(self._inverse_transform)
        return self.local_intersect(local_ray)

    @abstractmethod
    def local_intersect(self, r: ray):
        pass

    @abstractmethod
    def local_normal_at(self, p):
        pass

    def normal_at(self, world_point):
        object_normal = self.local_normal_at(world_point)
        world_normal = dot(transpose(self._inverse_transform), object_normal)
        return tp.normalize(tp.vector3(tp.x(world_normal), tp.y(world_normal), tp.z(world_normal)))

    @abstractmethod
    def set_transform(self, t):
        pass

    @abstractmethod
    def set_material(self, m):
        pass

    def __eq__(self, other):
        return self.material == other.material and np.allclose(self.transform, other.transform)
