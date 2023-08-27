from collections import namedtuple


def intersect(o, r):
    return o.intersect(r)


intersection = namedtuple('Intersection', 't object')


def t(x):
    return x[0]


def obj(x):
    return x[1]
