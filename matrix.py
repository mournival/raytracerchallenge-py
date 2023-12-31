from math import cos, sin

import numpy as np

from tuple import normalize, cross3


def matrix(table_data):
    return np.array(table_data, dtype='float')


def eye(n):
    return np.eye(n)


def array_equal(a, b):
    return np.array_equal(a, b)


def array_approximately_equal(a, b):
    return np.allclose(a, b, rtol=0.0001)


def cofactor(a, r, c):
    return (-1 if (r + c) % 2 else 1) * det(submatrix(a, r, c))


def det(a):
    return np.linalg.det(a)


def dot(a, b):
    return np.matmul(a, b)


def inverse(a):
    return np.linalg.inv(a)


def invertible(a):
    return det(a) != 0


def minor(a, r, c):
    return det(submatrix(a, r, c))


def rotation_x(radians):
    return np.array([
        [1, 0, 0, 0], [0, cos(radians), -sin(radians), 0], [0, sin(radians), cos(radians), 0], [0, 0, 0, 1]
    ])


def rotation_y(radians):
    return np.array([
        [cos(radians), 0, sin(radians), 0], [0, 1, 0, 0], [-sin(radians), 0, cos(radians), 0], [0, 0, 0, 1]
    ])


def rotation_z(radians):
    return np.array([
        [cos(radians), -sin(radians), 0, 0], [sin(radians), cos(radians), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]
    ])


def scaling(x, y, z, *_):
    return np.array([[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]])


def shearing(x_y, x_z, y_x, y_z, z_x, z_y):
    return np.array([[1, x_y, x_z, 0], [y_x, 1, y_z, 0], [z_x, z_y, 1, 0], [0, 0, 0, 1]])


def submatrix(a, m, n):
    return np.delete(np.delete(np.array(a), m, axis=0), n, axis=1)


def translation(x, y, z, *_):
    return np.array([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]])


def transpose(a):
    return np.transpose(a)


def view_transform(frm, to, up):
    forward = normalize(np.subtract(to, frm))
    left = cross3(forward, normalize(up))
    true_up = cross3(left, forward)
    return np.dot(np.array([left, true_up, -forward, [0, 0, 0, 1]]), translation(*(-frm)))
