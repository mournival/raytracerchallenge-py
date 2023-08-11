import numpy as np


def matrix(table_data):
    return np.array(table_data, dtype='float')


def eye(n):
    return np.eye(n)


def array_equal(A, B):
    return np.array_equal(A, B)


def det(A):
    return np.linalg.det(A)


def dot(a, b):
    return np.dot(a, b)


def matmul(A, B):
    return np.matmul(A, B)


def transpose(A):
    return np.transpose(A)
