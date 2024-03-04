from timeit import default_timer

import material as mat
import matrix
from canvas import Canvas
from color import color
from intersect import hit
from ray import ray, point_light, lighting
from sphere import sphere
from tuple import point, normalize


def main():  # pragma: no cover

    ray_origin = point(0, 0, -5)
    wall_z = 10
    wall_size = 8.0
    canvas_pixels = 400
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    c = Canvas(canvas_pixels, canvas_pixels)

    color(1, 0, 0)
    light = point_light(point(-10, 10, -10), color(1, 1, 1))
    shape = sphere(transform_matrix=matrix.eye(4), material=mat.material(color(1, 0.2, 1)))

    for y in range(canvas_pixels):
        world_y = half - pixel_size * y
        for x in range(canvas_pixels):
            world_x = -half + pixel_size * x
            p = point(world_x, world_y, wall_z)
            r = ray(ray_origin, normalize(p - ray_origin))

            xs = shape.intersect(r)

            if hit(xs):
                pt = r.position(hit(xs).t)
                normal = shape.normal_at(pt)
                eye = -r.direction
                c[x, y] = lighting(shape.material, light, pt, eye, normal)
            else:
                c[x, y] = color(0, 0, 0)
                # c[x, y] = color(y / canvas_pixels, y / canvas_pixels, y / canvas_pixels)

    with open('../images/chapter6.ppm', 'w', encoding="ascii") as f:
        for line in c.to_ppm():
            f.write(line)


if __name__ == '__main__':  # pragma: no cover
    start = default_timer()
    main()
    print(default_timer() - start)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
