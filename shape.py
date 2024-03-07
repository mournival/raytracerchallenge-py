from abc import ABC, abstractmethod

import numpy as np

import material as mat
from matrix import eye, inverse


class Shape(ABC):
    transform: np.array
    material: mat.Material

    def __init__(self, transform_matrix=eye(4), material: mat.material = mat.Material()):
        self.transform = transform_matrix
        self.material = material
        self._inverse_transform = inverse(self.transform)

    @abstractmethod
    def set_transform(self, t):
        pass

    @abstractmethod
    def set_material(self, m):
        pass

    def __eq__(self, other):
        return self.material == other.material and np.allclose(self.transform, other.transform)
