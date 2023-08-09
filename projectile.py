from collections import namedtuple

from tuple import point, normalize, vector
import matplotlib.pyplot as plt

projectile = namedtuple('Projectile', 'position velocity')
environment = namedtuple('Environment', 'gravity wind')


def tick(env: environment, proj: projectile) -> projectile:
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return projectile(position, velocity)

m = 10
p_naught = projectile(point(0, 1, 0), normalize(vector(1, 1, 0)) * m)
e = environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))


def main():
    p = p_naught
    t = 0
    ps = list()
    while p.position.y > 0:
        ps.append(p.position)
        p = tick(e, p)
        t += 1
    plt.axes(projection='3d')
    time = range(t)
    x = [p.x for p in ps]
    plt.xlabel( 'Tick')
    plt.ylabel( 'Distance')
    y = [p.y for p in ps]
    plt.plot(time, x, y)
    plt.plot(time, x, 0)
    plt.title('Projectile Path')
    plt.show()


if __name__ == '__main__':
    main()
