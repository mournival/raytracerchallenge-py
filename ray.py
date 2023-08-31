from collections import namedtuple

from matrix import dot

ray = namedtuple('Ray', 'origin direction')


def position(r, t):
    return r.origin + r.direction * t


def transform(r, m):
    return ray(dot(m, r.origin), dot(m, r.direction))
