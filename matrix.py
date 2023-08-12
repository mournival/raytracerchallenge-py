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


def dot(a, b):
    return np.dot(a, b)


def inverse(a):
    return np.linalg.inv(a)


def invertible(a):
    return det(a) != 0


def matmul(a, b):
    return np.matmul(a, b)


def minor(a, r, c):
    return det(submatrix(a, r, c))


def submatrix(a, m, n):
    return np.delete(np.delete(np.array(a), m, axis=0), n, axis=1)


def transpose(a):
    return np.transpose(a)
