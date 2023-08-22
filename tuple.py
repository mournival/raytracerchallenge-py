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


def point(_x, _y, _z):
    return np.array([_x, _y, _z, 1.0])


def tuple_trtc(_x, _y, _z, _w):
    return np.array([_x, _y, _z, _w])


def vector(_x, _y, _z):
    return np.array([_x, _y, _z, 0.0])


def cross(lhs, rhs):
    return vector(y(lhs) * z(rhs) - z(lhs) * y(rhs),
                  z(lhs) * x(rhs) - x(lhs) * z(rhs),
                  x(lhs) * y(rhs) - y(lhs) * x(rhs))


def dot(lhs, rhs):
    return np.dot(lhs, rhs)


def is_point(v):
    return w(v) == 1.0


def is_vector(v):
    return w(v) == 0.0


def magnitude(v):
    return math.sqrt(dot(v, v))


def normalize(v):
    return v / magnitude(v)
