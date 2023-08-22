from math import pi

from canvas import Canvas
from color import color
from matrix import translation, scaling, rotation_z
from tuple import point, dot, x, y

COLOR = color(1, 1, 1)


def axes(c: Canvas):
    p = round(c.width / 2)
    for n in range(round(c.width / 6), round(5 * c.width / 6)):
        c[n, p] = COLOR
        c[p, n] = COLOR


def scaled_translation(width):
    return dot(translation(width / 2, width / 2, 0),
               scaling(width / 3, width / 3, 0))


clr = color(1, 0, 0)


def clock(canvas, dots, dot_size):
    st = scaled_translation(canvas.width)
    sl = 2 * pi / dots
    half_dot = dot_size / 2
    for i in range(dots):
        p = dot(dot(st, rotation_z(sl * i)), point(0, 1, 0))
        for _c in range(dot_size):
            dot__c = y(p) - half_dot + _c
            p_half_dot = x(p) - half_dot
            for _r in range(dot_size):
                canvas[
                    round(p_half_dot + _r),
                    round(dot__c)
                ] = clr


def main():
    c = Canvas(900, 900)
    axes(c)
    clock(c, 12, 16)
    clock(c, 60, 4)

    with open('../images/clock.ppm', 'w', encoding="ascii") as f:
        for l in c.to_ppm():
            f.write(l)


if __name__ == '__main__':
    main()
