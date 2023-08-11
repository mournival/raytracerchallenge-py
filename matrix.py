import numpy as np


def matrix(table_data):
    return np.array(table_data, dtype='float')


def eye(n):
    return np.eye(n)


def array_equal(a, b):
    return np.array_equal(a, b)


def det(a):
    return np.linalg.det(a)


def dot(a, b):
    return np.dot(a, b)


def matmul(a, b):
    return np.matmul(a, b)


def submatrix(a, m, n):
    return np.delete(np.delete(np.array(a), m, axis=0), n, axis=1)


def transpose(a):
    return np.transpose(a)
