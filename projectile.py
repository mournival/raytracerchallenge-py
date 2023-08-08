from collections import namedtuple

from tuple import point, normalize, vector
import matplotlib.pyplot as plt

projectile = namedtuple('Projectile', 'position velocity')
environment = namedtuple('Environment', 'gravity wind')


def tick(env: environment, proj: projectile) -> projectile:
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return projectile(position, velocity)

m = 1
p_naught = projectile(point(0, 1, 0), normalize(vector(1, 1, 0)) * m)
e = environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))


def main():
    p = p_naught
    t = 0
    ps = list()
    while p.position.y > 0:
        ps.append(p.position.y)
        p = tick(e, p)
        t += 1
    plt.plot(range(t), ps)
    plt.xlabel('tick')
    plt.ylabel('height')
    plt.title('Projectile Altitude')
    plt.show()


if __name__ == '__main__':
    main()
