import math

from ray import ray
from tuple import point, dot


class Sphere(object):
    def intersect(self, r: ray):
        sphere_to_ray = r.origin - point(0, 0, 0)
        a = dot(r.direction, r.direction)
        b = 2 * dot(r.direction, sphere_to_ray)
        c = dot(sphere_to_ray, sphere_to_ray) - 1
        discriminant = b *b - 4 * a * c

        if discriminant < 0:
            return []
        d = math.sqrt(discriminant)
        return [(-b - d) / (2 * a), (-b + d) / (2 * a)]


sphere = Sphere
