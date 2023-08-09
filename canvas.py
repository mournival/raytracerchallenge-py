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
            r = round(p.red * 255)
            if r < 0:
                r = 0
            elif r > 255:
                r = 255
            g = round(p.green * 255)
            if g < 0:
                g = 0
            elif g > 255:
                g = 255
            b = round(p.blue * 255)
            if b < 0:
                b = 0
            elif b > 255:
                b = 255
            ppm = ppm + ' '.join([str(r), str(g), str(b)])
            count += 1
            if count % 5 == 0:
                ppm = ppm + '\n'
            else:
                ppm = ppm + ' '
        return ppm


if __name__ == '__main__':
    c = Canvas(10, 20)
    print(c.height)
    print(c.width)
    print(c.pixels())
    c[0, 0] = Color(1, 1, 1)
    print(c[0, 0])
