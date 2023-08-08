from collections import namedtuple


class Color(namedtuple('Color', 'red green blue')):
    def __add__(self, other):
        return Color(self.red + other.red, self.green + other.green, self.blue + other.blue)

    def __sub__(self, other):
        return Color(self.red - other.red, self.green - other.green, self.blue - other.blue)

    def __mul__(self, other):
        return Color(self.red * other, self.green * other, self.blue * other)


def hadamard_product(lhs: Color, rhs: Color) -> Color:
    return Color(lhs.red * rhs.red, lhs.green * rhs.green, lhs.blue * rhs.blue)