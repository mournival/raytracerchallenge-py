from canvas import Canvas
from color import color
from intersect import hit, intersect
from ray import ray
from sphere import sphere
from tuple import point, normalize


def main():
    ray_origin = point(0, 0, -5)
    wall_z = 10
    wall_size = 8.0
    canvas_pixels = 800
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    c = Canvas(canvas_pixels, canvas_pixels)
    red = color(1, 0, 0)
    shape = sphere()

    for y in range(canvas_pixels):
        world_y = half - pixel_size * y
        for x in range(canvas_pixels):
            world_x = -half + pixel_size * x
            p = point(world_x, world_y, wall_z)
            r = ray(ray_origin, normalize(p - ray_origin))

            xs = intersect(shape, r)

            if hit(xs):
                c[x, y] = red

    with open('../images/chapter5.ppm', 'w', encoding="ascii") as f:
        for line in c.to_ppm():
            f.write(line)


if __name__ == '__main__':
    main()
