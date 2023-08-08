import numpy as np

from color import Color


class Canvas(object):


    def __init__(self, width, height):
        self._data = np.empty((width, height), Color)
        for r in range(width):
            for c in range(height):
                self._data[r,c]= Color(0,0,0)
        self.width = self._data.shape[0]
        self.height = self._data.shape[1]

    def pixels(self):
        return list(self._data.flatten())

if __name__ == '__main__':
    c = Canvas(10, 20)
    print(c.height)
    print(c.width)
    print(c.pixels())