import numpy as np


def color(r: float = 1.0, g: float = 1.0, b: float = 1.0):
    return np.array([r, g, b])


def red(c):
    return c[0]


def green(c):
    return c[1]


def blue(c):
    return c[2]


def _clamp(c: float):
    v = round(c * 255)
    if v < 0:
        return "0"
    if v > 255:
        return "255"
    return str(v)


def clamp_color(c):
    return [_clamp(c[0]), _clamp(c[1]), _clamp(c[2])]


BLACK = color(0, 0, 0)
