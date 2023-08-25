from collections import namedtuple

ray = namedtuple('Ray', 'origin direction')


def position(r, t):
    return r.origin + r.direction * t
