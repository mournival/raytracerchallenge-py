from math import cos, sin

import numpy as np


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


# For 2D arrays, this subsumes def matmul(a,b) -> np.matmul(a, b), and allows scalar
# products, so is more flexible
def dot(a, b):
    return np.dot(a, b)


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
        [cos(radians), -sin(radians), 0, 0], [sin(radians), cos(radians),0, 0], [0, 0, 1, 0], [0, 0, 0, 1]
    ])


def scaling(x, y, z):
    return np.array([[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]])


def submatrix(a, m, n):
    return np.delete(np.delete(np.array(a), m, axis=0), n, axis=1)


def translation(x, y, z):
    return np.array([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]])


def transpose(a):
    return np.transpose(a)
