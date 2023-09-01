import math

from intersect import intersection
from matrix import eye, inverse
from ray import ray, transform
from tuple import point, dot


class Sphere(object):

    def __init__(self, transform=eye(4)):
        self.transform = transform

    def intersect(self, r: ray):
        tray = transform(r, inverse(self.transform))
        sphere_to_ray = tray.origin - point(0, 0, 0)
        a = dot(tray.direction, tray.direction)
        b = 2 * dot(tray.direction, sphere_to_ray)
        c = dot(sphere_to_ray, sphere_to_ray) - 1
        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return []
        d = math.sqrt(discriminant)
        return [intersection((-b - d) / (2 * a), self), intersection((-b + d) / (2 * a), self)]


sphere = Sphere


def set_transform(o, t):
    return sphere(t)
