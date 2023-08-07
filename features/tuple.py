from collections import namedtuple


class Tuple(namedtuple('Tuple', [('x'), ('y'), ('z'), ('w')])):

    def isPoint(self) -> bool:
        return self.w == 1.0

    def isVector(self) -> bool:
        return self.w == 0.0

    def __add__(self, other):
        return Tuple(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return Tuple(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

def point(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 1.0)


def vector(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 0.0)
