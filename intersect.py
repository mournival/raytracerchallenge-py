from collections import namedtuple
from typing import List

intersection = namedtuple('Intersection', 't object')


def intersect(o, r) -> List[intersection]:
    return o.intersect(r)


def intersections(*t1):
    return [i for i in sorted(t1, key=lambda i: i.t)]


def hit(xs: List[intersection]):
    return next((x for x in xs if x.t >= 0), None)
