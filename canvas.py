import numpy as np

from color import Color


class Canvas(object):

    def __init__(self, width, height):
        self._data = np.empty((width, height), Color)
        for row in range(width):
            for col in range(height):
                self._data[row, col] = Color(0, 0, 0)
        self.width, self.height = self._data.shape

    def pixels(self):
        return list(self._data.flatten())

    def __getitem__(self, indices):
        return self._data[indices]

    def __setitem__(self, key, value):
        self._data[key] = value

    def to_ppm(self):
        return '\n'.join(['P3', f"{self.width} {self.height}", "255", *self._pixel_rows()]) + '\n'

    def _pixel_rows(self):
        pr = list()
        for pixels in [self.pixels()[x: x + self.width] for x in range(0, self.width * self.height, self.width)]:
            pr.append(' '.join([' '.join(p.clamp_color(0, 255)) for p in pixels]))
        return pr

    def fill(self, color: Color):
        self._data.fill(color)


if __name__ == '__main__':
    c = Canvas(2, 2)
    # print(c.height)
    # print(c.width)
    c.fill(Color(1, 2, 3))
    c[0, 0] = Color(1, 1, 1)
    # print(c.pixels())
    print(c.to_ppm())
