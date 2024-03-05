import math

import numpy as np

from canvas import Canvas
from matrix import eye, inverse, dot
from ray import ray
from tuple import point, normalize
from world import color_at


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
        self._inverse_transform = inverse(self.transform)
        self._pixel_size()

    def set_transform(self, t):
        return Camera(self.hsize, self.vsize, self.field_of_view, t)

    def ray_for_pixel(self, px, py):
        offset_x = (px + 0.5) * self.pixel_size
        offset_y = (py + 0.5) * self.pixel_size

        world_x = self.half_width - offset_x
        world_y = self.half_height - offset_y

        pixel = dot(self._inverse_transform, point(world_x, world_y, -1))
        origin = dot(self._inverse_transform, point(0, 0, 0))
        direction = normalize(pixel - origin)
        return ray(origin, direction)

    def render(self, world):
        image = Canvas(self.hsize, self.vsize)
        for y in range(self.vsize):
            for x in range(self.hsize):
                r = self.ray_for_pixel(x, y)
                c = color_at(world, r)
                image[x, y] = c
        return image

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


def ray_for_pixel(camera, px, py):
    return camera.ray_for_pixel(px, py)
