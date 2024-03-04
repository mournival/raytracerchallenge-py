import datetime
import math

import numpy as np

import matrix
from camera import Camera
from color import color
from matrix import scaling
from ray import material, point_light
from sphere import sphere
from tuple import point, vector3
from world import World


def create_image():
    floor = sphere(scaling(10, 0.01, 10), material(color=color(1, 0.9, 0.9), specular=0))
    left_wall = sphere(np.matmul(matrix.translation(0, 0, 5), np.matmul(matrix.rotation_y(- math.pi / 4),
                                                                        np.matmul(matrix.rotation_x(math.pi / 2),
                                                                                  scaling(10, 0.01, 10)))),
                       floor.material)
    right_wall = sphere(np.matmul(matrix.translation(0, 0, 5), np.matmul(matrix.rotation_y(math.pi / 4),
                                                                         np.matmul(matrix.rotation_x(math.pi / 2),
                                                                                   scaling(10, 0.01, 10)))),
                        floor.material)
    middle = sphere(matrix.translation(-0.5, 1, 0.5), material(color=color(0.1, 1, 0.5), diffuse=0.7, specular=0.3))
    right = sphere(np.matmul(matrix.translation(1.5, 0.5, -0.5), scaling(0.5, 0.5, 0.5)),
                   material(color=color(0.5, 1, 0.1), diffuse=0.7, specular=0.3))
    left = sphere(np.matmul(matrix.translation(-1.5, 0.33, -0.75), scaling(0.33, 0.33, 0.33)),
                  material(color=color(1.0, 0.8, 0.1), diffuse=0.7, specular=0.3))
    w = World(point_light(point(-10, 10, -10), color(1, 1.1)), [floor, left_wall, right_wall, middle, left, right])
    c = Camera(1000, 500, math.pi / 3, matrix.view_transform(point(0, 1.5, -5), point(0, 1, 0), vector3(0, 1, 0)))
    image = c.render(w)
    return image


def main():  # pragma: no cover
    image = create_image()

    with open('../images/chapter7.ppm', 'w', encoding="ascii") as f:
        for line in image.to_ppm():
            f.write(line)


if __name__ == '__main__':  # pragma: no cover
    start = datetime.datetime.now()
    main()
    print(f"{datetime.datetime.now() - start}")
