from dataclasses import dataclass
from typing import List


@dataclass
class Intersection:
    t: float
    object: any

    def intersect(self, r):
        return self.object.intersect(r)


intersection = Intersection


def intersections(*t1):
    return [i for i in sorted(t1, key=lambda i: i.t)]


def hit(xs: List[intersection]):
    return next((x for x in xs if x.t >= 0), None)
