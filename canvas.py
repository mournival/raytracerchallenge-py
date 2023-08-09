import numpy as np

from color import Color


class Canvas(object):

    def __init__(self, width, height):
        self._data = np.empty((width, height), Color)
        for r in range(width):
            for c in range(height):
                self._data[r, c] = Color(0, 0, 0)
        self.width, self.height = self._data.shape

    def pixels(self):
        return list(self._data.flatten())

    def __getitem__(self, indices):
        return self._data[indices]

    def __setitem__(self, key, value):
        self._data[key] = value

    def to_ppm(self):
        return f"""P3
{self.width} {self.height}
255
{self._pixel_rows()}"""

    def _pixel_rows(self):
        ppm = ""
        count = 0
        for p in self.pixels():
            count += 1
            ppm = ppm + ' '.join(p.clamp_color(0, 255))
            ppm = self.add_separator(count, ppm)
        return ppm

    def add_separator(self, count, ppm):
        if count % self.width == 0:
            return ppm + '\n'
        return ppm + ' '


if __name__ == '__main__':
    c = Canvas(10, 20)
    print(c.height)
    print(c.width)
    print(c.pixels())
    c[0, 0] = Color(1, 1, 1)
    print(c[0, 0])
