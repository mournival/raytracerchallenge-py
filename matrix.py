import numpy as np


def eye(n):
    return np.eye(n)


def det(A):
    return np.linalg.det(A)


def matrix(table_data):
    return np.array(table_data, dtype='float')


def transpose(A):
    return np.transpose(A)


def matmul(A, B):
    return np.matmul(A, B)


def array_equal(A, B):
    return np.array_equal(A, B)
