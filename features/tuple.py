from collections import namedtuple


class Tuple(namedtuple('Tuple', [('x'), ('y'), ('z'), ('w')])):

    def isPoint(self) -> bool:
        return self.w == 1.0

    def isVector(self) -> bool:
        return self.w == 0.0


def point(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 1.0)


def vector(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 0.0)
