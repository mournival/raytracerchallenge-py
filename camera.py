import numpy as np

from matrix import eye


class Camera:
    hsize: int
    vsize: int
    field_of_view: float
    transform: np.array
    
    def __init__(self, hsize, vsize, field_of_view, transform = eye(4)):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = transform
        