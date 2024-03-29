import material as mat
import tuple as tp
from intersect import EPSILON, intersection
from matrix import eye
from ray import Ray
from shape import Shape


class Plane(Shape):

    def __init__(self, transform_matrix=eye(4), material=mat.material()):
        super().__init__(transform_matrix, material)

    def local_intersect(self, r: Ray):
        if abs(tp.y(r.direction)) < EPSILON:
            return []
        return [intersection(-tp.y(r.origin) / tp.y(r.direction), self)]

    def local_normal_at(self, p):
        return tp.vector3(0, 1, 0)

    def set_transform(self, t):
        return Plane(t, self.material)

    def set_material(self, m):
        return Plane(self.transform, m)


Plane = Plane
