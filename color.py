from collections import namedtuple


def _clamp(c, min_val, max_val):
    v = round(c * max_val)
    if v < min_val:
        return str(min_val)
    if v > max_val:
        return str(max_val)
    return str(v)


class Color(namedtuple('Color', 'red green blue')):
    def __add__(self, other):
        return Color(self.red + other.red, self.green + other.green, self.blue + other.blue)

    def __sub__(self, other):
        return Color(self.red - other.red, self.green - other.green, self.blue - other.blue)

    def __mul__(self, other):
        return Color(self.red * other, self.green * other, self.blue * other)

    def clamp_color(self, min_val, max_val):
        return [_clamp(self.red, min_val, max_val),
                _clamp(self.green, min_val, max_val),
                _clamp(self.blue, min_val, max_val)]


def color(r, g, b):
    return Color(r, g, b)


def hadamard_product(lhs: Color, rhs: Color) -> Color:
    return Color(lhs.red * rhs.red, lhs.green * rhs.green, lhs.blue * rhs.blue)
