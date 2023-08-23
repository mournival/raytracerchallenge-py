import numpy as np

from color import color, clamp_color, BLACK


def clamp_line(line):
    if (len(line)) < 71:
        return [line]
    for i in range(70, 0, -1):
        if line[i] == ' ':
            return [line[: i]] + clamp_line(line[i + 1:])
    return [line]


class Canvas(object):

    def __init__(self, width, height):
        self._data = np.empty(shape=(width, height), dtype=type(BLACK))
        self._data.fill(BLACK)
        self.width, self.height = self._data.shape

    def pixels(self):
        return self._data.flatten(order='F')

    def __getitem__(self, indices):
        return self._data[indices]

    def __setitem__(self, key, value):
        self._data[key] = value

    def to_ppm(self):
        return '\n'.join(['P3', f"{self.width} {self.height}", "255", *self._pixel_rows()]) + '\n'

    def _pixel_rows(self):
        pr = list()
        pixels = self.pixels()
        rows = [pixels[x: x + self.width] for x in range(0, self.width * self.height, self.width)]
        for row in rows:
            line = ' '.join([' '.join(clamp_color(p, 0, 255)) for p in row])
            pr += clamp_line(line)
        return pr

    def fill(self, clr):
        self._data.fill(clr)


if __name__ == '__main__':
    c = Canvas(2, 2)
    # print(c.height)
    # print(c.width)
    c.fill(color(1, 2, 3))
    c[0, 0] = color(1, 1, 1)
    # print(c.pixels())
    print(c.to_ppm())
