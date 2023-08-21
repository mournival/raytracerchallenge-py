import math

import numpy as np


def x(v):
    return v[0]


def y(v):
    return v[1]


def z(v):
    return v[2]


def w(v):
    return v[3]


def point(x: float, y: float, z: float):
    return np.array([x, y, z, 1.0])


def tuple_trtc(x, y, z, w):
    return np.array([x, y, z, w])


def vector(x: float, y: float, z: float):
    return np.array([x, y, z, 0.0])


def cross(lhs, rhs):
    return vector(y(lhs) * z(rhs) - z(lhs) * y(rhs),
                  z(lhs) * x(rhs) - x(lhs) * z(rhs),
                  x(lhs) * y(rhs) - y(lhs) * x(rhs))


def dot(lhs, rhs) -> float:
    return np.dot(lhs, rhs)


def is_point(v) -> bool:
    return w(v) == 1.0


def is_vector(v) -> bool:
    return w(v) == 0.0


def magnitude(v) -> float:
    return math.sqrt(dot(v, v))


def normalize(v):
    return v / magnitude(v)
