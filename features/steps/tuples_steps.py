import math
from math import sqrt

from behave import use_step_matcher, given, when, then, step

from color import Color, hadamard_product
from features.environment import assert_equal, assert_approximate_xyz, assert_approximate_rgb
from tuple import Tuple, point, vector, magnitude, normalize, dot, cross

use_step_matcher("parse")


@given('{:w} ← tuple({:g}, {:g}, {:g}, {:g})')
def step_tuple_create(context, a, x, y, z, w):
    context.tuples[a] = Tuple(x, y, z, w)


@then("{:w}.{:w} = {:g}")
def step_tuple_field_equals(context, name, field, expected):
    assert context.tuples[name].__getattribute__(
        field) == expected, f"{context.tuples[name].__getattribute__(field).field} != {expected}"


@step("{:w} is a point")
def step_tuple_is_point(context, name):
    assert context.tuples[name].is_point(), f"{context.tuples[name]} is NOT a point"


@step("{:w} is not a vector")
def step_tuple_is_not_vector(context, name):
    assert ~context.tuples[name].is_vector(), f"{context.tuples[name]} is a vector"


@step("{:w} is not a point")
def step_tuple_is_not_point(context, name):
    assert ~context.tuples[name].is_point(), f"{context.tuples[name]} is a point"


@step("{:w} is a vector")
def step_tuple_is_vector(context, name):
    assert context.tuples[name].is_vector(), f"{context.tuples[name]} is NOT a vector"


@given("{:w} ← point({:g}, {:g}, {:g})")
def step_tuple_create_point(context, name, x, y, z):
    context.tuples[name] = point(x, y, z)


@then("-{:w} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_negate(context, name, x, y, z, w):
    assert_equal(-context.tuples[name], Tuple(x, y, z, w))


@then("{:w} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_equals(context, name, x, y, z, w):
    assert_equal(context.tuples[name], Tuple(x, y, z, w))


@given("{:w} ← vector({:g}, {:g}, {:g})")
def step_tuple_create_vector(context, name, x, y, z):
    context.tuples[name] = vector(x, y, z)


@given("{:w} ← vector({:g}/√{:g}, {:g}/√{:g}, {:g}/√{:g})")
def step_tuple_create_vector_with_radicals(context, name, x1, x2, y1, y2, z1, z2):
    context.tuples[name] = vector(x1 / math.sqrt(x2), y1 / math.sqrt(y2), z1 / math.sqrt(z2))


@then("{:w} + {:w} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_addition(context, a, b, x, y, z, w):
    assert_equal(context.tuples[a] + context.tuples[b], Tuple(x, y, z, w))


@then("{:w} - {:w} = vector({:g}, {:g}, {:g})")
def step_tuple_vector_subtraction(context, a, b, x, y, z):
    assert_equal(context.tuples[a] - context.tuples[b], vector(x, y, z))


@then("{:w} - {:w} = point({:g}, {:g}, {:g})")
def step_tuple_point_subtraction(context, a, b, x, y, z):
    assert_equal(context.tuples[a] - context.tuples[b], point(x, y, z))


@then("{:w} * {:g} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_scalar_multiplication(context, a, c, x, y, z, w):
    assert_equal(context.tuples[a] * c, Tuple(x, y, z, w))


@then("{:w} / {:g} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_scalar_division(context, a, c, x, y, z, w):
    assert_equal(context.tuples[a] / c, Tuple(x, y, z, w))


@then("magnitude({:w}) = {:g}")
def step_tuple_magnitude_equals(context, a, expected):
    assert_equal(magnitude(context.tuples[a]), expected)


@then("magnitude({:w}) = approximately {:g}")
def step_tuple_magnitude_approximately_equals(context, a, expected):
    assert_equal(magnitude(context.tuples[a]), expected)


@then("magnitude({:w}) = √{:g}")
def step_tuple_magnitude_equals_radical(context, a, b):
    assert_equal(magnitude(context.tuples[a]), sqrt(b))


@then("normalize({:w}) = vector({:g}, {:g}, {:g})")
def step_tuple_normalized_equals(context, v, x, y, z):
    assert_equal(normalize(context.tuples[v]), vector(x, y, z))


@then("normalize({:w}) = approximately vector({:g}, {:g}, {:g})")
def step_tuple_normalized_approximately_equals(context, v, x, y, z):
    assert_approximate_xyz(normalize(context.tuples[v]), x, y, z)


@when("{:w} ← normalize({:w})")
def step_tuple_create_normalized(context, norm, v):
    context.tuples[norm] = normalize(context.tuples[v])


@then("dot({:w}, {:w}) = {:g}")
def step_tuple_dot_product(context, a, b, expected):
    assert_equal(dot(context.tuples[a], context.tuples[b]), expected)


@then("cross({:w}, {:w}) = vector({:g}, {:g}, {:g})")
def step_tuple_cross_product(context, a, b, x, y, z):
    assert_equal(cross(context.tuples[a], context.tuples[b]), vector(x, y, z))


@then("{:w} = vector({:g}, {:g}, {:g})")
def step_tuple_equal(context, v, x, y, z):
    assert_equal(context.tuples[v], vector(x, y, z))


@then("{:w} = approximately vector({:g}, {:g}, {:g})")
def step_tuple_approximately_equal(context, v, x, y, z):
    assert_approximate_xyz(context.tuples[v], x, y, z)


@then("magnitude({:w}) = √{:g}")
def step_tuple_magnitude(context, a, c):
    assert_equal(magnitude(context.tuples[a]), sqrt(c))


@given("{:w} ← color({:g}, {:g}, {:g})")
def step_tuple_create_color(context, c, r, g, b):
    context.tuples[c] = Color(r, g, b)


@then("{:w} + {:w} = color({:g}, {:g}, {:g})")
def step_tuple_color_addition(context, a, b, red, green, blue):
    assert_equal(context.tuples[a] + context.tuples[b], Color(red, green, blue))


@then("{:w} - {:w} = color({:g}, {:g}, {:g})")
def step_tuple_color_subtraction(context, a, b, red, green, blue):
    assert_approximate_rgb(context.tuples[a] - context.tuples[b], red, green, blue)


@then("{:w} * {:w} = color({:g}, {:g}, {:g})")
def step_tuple_color_multiplication(context, a, b, red, green, blue):
    try:
        b = float(b)
        actual = context.tuples[a] * b
    except ValueError:
        actual = hadamard_product(context.tuples[a], context.tuples[b])
    assert_approximate_rgb(actual, red, green, blue)
