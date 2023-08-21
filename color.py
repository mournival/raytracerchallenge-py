import numpy as np


def color(r: float, g: float, b: float):
    return np.array([r, g, b])


def red(c):
    return c[0]


def green(c):
    return c[1]


def blue(c):
    return c[2]


def _clamp(c: float, min_val: int, max_val: int) -> str:
    v = round(c * max_val)
    if v < min_val:
        return str(min_val)
    if v > max_val:
        return str(max_val)
    return str(v)


def clamp_color(c, min_val, max_val):
    return [_clamp(c[0], min_val, max_val),
            _clamp(c[1], min_val, max_val),
            _clamp(c[2], min_val, max_val)]


BLACK = color(0, 0, 0)
