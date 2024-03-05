import numpy as np

import material as mat
from matrix import eye
from shape import Shape


class TestShape(Shape):
    def __init__(self, transform_matrix=eye(4), material: mat.material = mat.Material()):
        super().__init__(transform_matrix, material)

    def set_transform(self, t) -> np.array:
        return TestShape(t, self.material)
