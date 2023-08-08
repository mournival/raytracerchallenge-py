import math
from collections import namedtuple


class Tuple(namedtuple('Tuple', "x y z w")):

    def is_point(self) -> bool:
        return self.w == 1.0

    def is_vector(self) -> bool:
        return self.w == 0.0

    def __add__(self, other):
        return Tuple(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return Tuple(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __mul__(self, other):
        return Tuple(self.x * other, self.y * other, self.z * other, self.w * other)

    def __truediv__(self, other):
        return Tuple(self.x / other, self.y / other, self.z / other, self.w / other)

    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)


def dot(lhs: Tuple, rhs: Tuple) -> Tuple:
    return lhs.x * rhs.x + lhs.y * rhs.y + lhs.z * rhs.z + lhs.w * rhs.w


def magnitude(v: Tuple):
    return math.sqrt(dot(v, v))


def point(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 1.0)


def vector(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 0.0)


def normalize(v: Tuple) -> Tuple:
    return v / magnitude(v)
