import math
from math import sqrt

from behave import *

from tuple import Tuple, point, vector, magnitude, normalize, dot, cross

use_step_matcher("parse")


@given('{:w} ← tuple({:g}, {:g}, {:g}, {:g})')
def step_impl(context, a, x, y, z, w):
    context.tuples[a] = Tuple(x, y, z, w)


@then("{:w}.{:w} = {:g}")
def step_impl(context, name, field, expected):
    assert (context.tuples[name].__getattribute__(field) == expected)


@step("{:w} is a point")
def step_impl(context, name):
    assert (context.tuples[name].is_point())


@step("{:w} is not a vector")
def step_impl(context, name):
    assert (~context.tuples[name].is_vector())


@step("{:w} is not a point")
def step_impl(context, name):
    assert (~context.tuples[name].is_point())


@step("{:w} is a vector")
def step_impl(context, name):
    assert (context.tuples[name].is_vector())


@given("{:w} ← point({:g}, {:g}, {:g})")
def step_impl(context, name, x, y, z):
    context.tuples[name] = point(x, y, z)


@then("-{:w} = tuple({:g}, {:g}, {:g}, {:g})")
def step_impl(context, name, x, y, z, w):
    assert (-context.tuples[name] == Tuple(x, y, z, w))


@then("{:w} = tuple({:g}, {:g}, {:g}, {:g})")
def step_impl(context, name, x, y, z, w):
    assert (context.tuples[name] == Tuple(x, y, z, w))


@given("{:w} ← vector({:g}, {:g}, {:g})")
def step_impl(context, name, x, y, z):
    context.tuples[name] = vector(x, y, z)


@given("{:w} ← vector({:g}/√{:g}, {:g}/√{:g}, {:g}/√{:g})")
def step_impl(context, name, x1, x2, y1, y2, z1, z2):
    context.tuples[name] = vector(x1 / math.sqrt(x2), y1 / math.sqrt(y2), z1 / math.sqrt(z2))


@then("{:w} + {:w} = tuple({:g}, {:g}, {:g}, {:g})")
def step_impl(context, a, b, x, y, z, w):
    assert (context.tuples[a] + context.tuples[b] == Tuple(x, y, z, w))


@then("{:w} - {:w} = vector({:g}, {:g}, {:g})")
def step_impl(context, a, b, x, y, z):
    assert (context.tuples[a] - context.tuples[b] == vector(x, y, z))


@then("{:w} - {:w} = point({:g}, {:g}, {:g})")
def step_impl(context, a, b, x, y, z):
    assert (context.tuples[a] - context.tuples[b] == point(x, y, z))


@then("{:w} * {:g} = tuple({:g}, {:g}, {:g}, {:g})")
def step_impl(context, a, c, x, y, z, w):
    assert (context.tuples[a] * c == Tuple(x, y, z, w))


@then("{:w} / {:g} = tuple({:g}, {:g}, {:g}, {:g})")
def step_impl(context, a, c, x, y, z, w):
    assert (context.tuples[a] / c == Tuple(x, y, z, w))


@then("magnitude({:w}) = {:g}")
def step_impl(context, a, expected):
    assert (magnitude(context.tuples[a]) == expected)


@then("magnitude({:w}) = √{:g}")
def step_impl(context, a, expected):
    assert (magnitude(context.tuples[a]) == sqrt(expected))


EPSILON = 0.0001


@then("normalize({:w}) = vector({:g}, {:g}, {:g})")
def step_impl(context, v, x, y, z):
    assert (normalize(context.tuples[v]) == vector(x, y, z))


@when("{:w} ← normalize({:w})")
def step_impl(context, norm, v):
    context.tuples[norm] = normalize(context.tuples[v])


@then("dot({:w}, {:w}) = {:g}")
def step_impl(context, a, b, expected):
    assert (abs(dot(context.tuples[a], context.tuples[b]) - expected) < EPSILON)


@then("cross({:w}, {:w}) = vector({:g}, {:g}, {:g})")
def step_impl(context, a, b, x, y, z):
    assert (cross(context.tuples[a], context.tuples[b]) == vector(x, y, z))


@then("normalize({:w}) = approximately vector({:g}, {:g}, {:g})")
def step_impl(context, v, x, y, z):
    actual = normalize(context.tuples[v])
    assert (abs((actual.x - x)) < EPSILON)
    assert (abs((actual.y - y)) < EPSILON)
    assert (abs((actual.z - z)) < EPSILON)


@then("{:w} = vector({:g}, {:g}, {:g})")
def step_impl(context, v, x, y, z):
    assert (context.tuples[v] == vector(x, y, z))


@then("{:w} = approximately vector({:g}, {:g}, {:g})")
def step_impl(context, v, x, y, z):
    actual = context.tuples[v]
    assert (abs((actual.x - x)) < EPSILON)
    assert (abs((actual.y - y)) < EPSILON)
    assert (abs((actual.z - z)) < EPSILON)

@then("magnitude({:w}) = √{:g}")
def step_impl(context, a, expected):
    assert (magnitude(context.tuples[a]) == sqrt(expected))
