from collections import namedtuple
from typing import List

intersection = namedtuple('Intersection', 't object')


def intersect(o, r) -> List[float]:
    return o.intersect(r)


def intersections(t1, t2):
    return [i for i in sorted([t1, t2], key=t)]


def t(x):
    return x[0]

