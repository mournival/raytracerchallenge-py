import math

import numpy as np

from matrix import eye


class Camera:
    hsize: int
    vsize: int
    field_of_view: float
    transform: np.array

    def __init__(self, hsize, vsize, field_of_view, transform=eye(4)):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = transform
        self._pixel_size()

    def _pixel_size(self):
        half_view = math.tan(self.field_of_view / 2)
        aspect = self.hsize / self.vsize

        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect
        else:
            self.half_width = half_view * aspect
            self.half_height = half_view
        self.pixel_size = self.half_width * 2 / self.hsize
