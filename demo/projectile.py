from collections import namedtuple
from math import floor

import matplotlib.pyplot as plt

from canvas import Canvas
from color import color
from tuple import point, normalize, vector, x, y

projectile = namedtuple('Projectile', 'position velocity')
environment = namedtuple('Environment', 'gravity wind')


def tick(env: environment, proj: projectile) -> projectile:
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return projectile(position, velocity)


def main():
    start = point(0, 1, 0)
    velocity = normalize(vector(1, 1.8, 0)) * 11.25
    p = projectile(start, velocity)
    gravity = vector(0, -0.1, 0)
    wind = vector(-0.01, 0, 0)
    e = environment(gravity, wind)
    c = Canvas(900, 500)

    t = 0
    ps = list()
    while y(p.position) > 0:
        ps.append(p.position)
        if 499 - floor(y(p.position)) == 502:
            pass
        c[floor(x(p.position)), 499 - floor(y(p.position))] = color(1, 1, 1)
        p = tick(e, p)
        t += 1
    print(c.to_ppm())

    # Plot
    plt.axes(projection='3d')
    time = range(t)
    px = [x(p) for p in ps]
    plt.xlabel('Tick')
    plt.ylabel('Distance')
    py = [y(p) for p in ps]
    plt.plot(time, px, py)
    plt.plot(time, py, 0)
    plt.title('Projectile Path')
    plt.show()


if __name__ == '__main__':
    main()
