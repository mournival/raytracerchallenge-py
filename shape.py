from abc import ABC, abstractmethod

import numpy as np

import material as mat
from matrix import eye


class Shape(ABC):
    transform: np.array
    material: mat.Material

    def __init__(self, transform_matrix=eye(4), material: mat.material = mat.Material()):
        self.transform = transform_matrix
        self.material = material

    @abstractmethod
    def set_transform(self, t) -> np.array:
        pass
