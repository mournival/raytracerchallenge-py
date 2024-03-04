import numpy as np

import material as mat
from matrix import eye
from shape import Shape


class test_shape(Shape):
    def __init__(self, transform_matrix=eye(4), material: mat.material = mat.Material()):
        self.transform = transform_matrix
        self.material = material

    def set_transform(self, t) -> np.array:
        return test_shape(t, self.material)
