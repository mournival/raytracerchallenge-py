import math

from behave import use_step_matcher, given, when, then, step, register_type

from color import Color, hadamard_product
from features.environment import assert_equal, assert_approximate_xyz, assert_approximate_rgb, parse_ratio
from tuple import Tuple, point, vector, magnitude, normalize, dot, cross

use_step_matcher("parse")

register_type(rn=parse_ratio)


@given('{:w} ← tuple({:g}, {:g}, {:g}, {:g})')
def step_tuple_create(context, a, x, y, z, w):
    context.scenario_vars[a] = Tuple(x, y, z, w)


@then("{:w}.{:w} = {:g}")
def step_tuple_field_equals(context, name, field, expected):
    assert context.scenario_vars[name].__getattribute__(
        field) == expected, f"{context.scenario_vars[name].__getattribute__(field).field} != {expected}"


@step("{:w} is a point")
def step_tuple_is_point(context, name):
    assert context.scenario_vars[name].is_point(), f"{context.scenario_vars[name]} is NOT a point"


@step("{:w} is not a vector")
def step_tuple_is_not_vector(context, name):
    assert ~context.scenario_vars[name].is_vector(), f"{context.scenario_vars[name]} is a vector"


@step("{:w} is not a point")
def step_tuple_is_not_point(context, name):
    assert ~context.scenario_vars[name].is_point(), f"{context.scenario_vars[name]} is a point"


@step("{:w} is a vector")
def step_tuple_is_vector(context, name):
    assert context.scenario_vars[name].is_vector(), f"{context.scenario_vars[name]} is NOT a vector"


@given("{:w} ← point({:g}, {:g}, {:g})")
def step_tuple_create_point(context, name, x, y, z):
    context.scenario_vars[name] = point(x, y, z)


@then("-{:w} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_negate(context, name, x, y, z, w):
    assert_equal(-context.scenario_vars[name], Tuple(x, y, z, w))


@then("{:w} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_equals(context, name, x, y, z, w):
    assert_equal(context.scenario_vars[name], Tuple(x, y, z, w))


@given("{:w} ← vector({:g}, {:g}, {:g})")
def step_tuple_create_vector(context, name, x, y, z):
    context.scenario_vars[name] = vector(x, y, z)


@given("{:w} ← vector({:g}/√{:g}, {:g}/√{:g}, {:g}/√{:g})")
def step_tuple_create_vector_with_radicals(context, name, x1, x2, y1, y2, z1, z2):
    context.scenario_vars[name] = vector(x1 / math.sqrt(x2), y1 / math.sqrt(y2), z1 / math.sqrt(z2))


@then("{:w} + {:w} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_addition(context, a, b, x, y, z, w):
    assert_equal(context.scenario_vars[a] + context.scenario_vars[b], Tuple(x, y, z, w))


@then("{:w} - {:w} = vector({:g}, {:g}, {:g})")
def step_tuple_vector_subtraction(context, a, b, x, y, z):
    assert_equal(context.scenario_vars[a] - context.scenario_vars[b], vector(x, y, z))


@then("{:w} - {:w} = point({:g}, {:g}, {:g})")
def step_tuple_point_subtraction(context, a, b, x, y, z):
    assert_equal(context.scenario_vars[a] - context.scenario_vars[b], point(x, y, z))


@then("{:w} * {:g} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_scalar_multiplication(context, a, c, x, y, z, w):
    assert_equal(context.scenario_vars[a] * c, Tuple(x, y, z, w))


@then("{:w} / {:g} = tuple({:g}, {:g}, {:g}, {:g})")
def step_tuple_scalar_division(context, a, c, x, y, z, w):
    assert_equal(context.scenario_vars[a] / c, Tuple(x, y, z, w))


@then("magnitude({:w}) = {:rn}")
def step_tuple_magnitude_equals(context, a, expected):
    assert_equal(magnitude(context.scenario_vars[a]), expected)


@then("magnitude({:w}) = {:g}")
def step_tuple_magnitude_equals(context, a, expected):
    assert_equal(magnitude(context.scenario_vars[a]), expected)


@then("magnitude({:w}) = approximately {:g}")
def step_tuple_magnitude_approximately_equals(context, a, expected):
    assert_equal(magnitude(context.scenario_vars[a]), expected)


@then("magnitude({:w}) = {:rn}}")
def step_tuple_magnitude_equals_radical(context, a, expected):
    assert_equal(magnitude(context.scenario_vars[a]), expected)


@then("normalize({:w}) = vector({:g}, {:g}, {:g})")
def step_tuple_normalized_equals(context, v, x, y, z):
    assert_equal(normalize(context.scenario_vars[v]), vector(x, y, z))


@then("normalize({:w}) = approximately vector({:g}, {:g}, {:g})")
def step_tuple_normalized_approximately_equals(context, v, x, y, z):
    assert_approximate_xyz(normalize(context.scenario_vars[v]), x, y, z)


@when("{:w} ← normalize({:w})")
def step_tuple_create_normalized(context, norm, v):
    context.scenario_vars[norm] = normalize(context.scenario_vars[v])


@then("dot({:w}, {:w}) = {:g}")
def step_tuple_dot_product(context, a, b, expected):
    assert_equal(dot(context.scenario_vars[a], context.scenario_vars[b]), expected)


@then("cross({:w}, {:w}) = vector({:g}, {:g}, {:g})")
def step_tuple_cross_product(context, a, b, x, y, z):
    assert_equal(cross(context.scenario_vars[a], context.scenario_vars[b]), vector(x, y, z))


@then("{:w} = vector({:g}, {:g}, {:g})")
def step_tuple_equal(context, v, x, y, z):
    assert_equal(context.scenario_vars[v], vector(x, y, z))


@then("{:w} = approximately vector({:g}, {:g}, {:g})")
def step_tuple_approximately_equal(context, v, x, y, z):
    assert_approximate_xyz(context.scenario_vars[v], x, y, z)


@given("{:w} ← color({:g}, {:g}, {:g})")
def step_tuple_create_color(context, c, r, g, b):
    context.scenario_vars[c] = Color(r, g, b)


@then("{:w} + {:w} = color({:g}, {:g}, {:g})")
def step_tuple_color_addition(context, a, b, red, green, blue):
    assert_equal(context.scenario_vars[a] + context.scenario_vars[b], Color(red, green, blue))


@then("{:w} - {:w} = color({:g}, {:g}, {:g})")
def step_tuple_color_subtraction(context, a, b, red, green, blue):
    assert_approximate_rgb(context.scenario_vars[a] - context.scenario_vars[b], red, green, blue)


@then("{:w} * {:w} = color({:g}, {:g}, {:g})")
def step_tuple_color_multiplication(context, a, b, red, green, blue):
    try:
        b = float(b)
        actual = context.scenario_vars[a] * b
    except ValueError:
        actual = hadamard_product(context.scenario_vars[a], context.scenario_vars[b])
    assert_approximate_rgb(actual, red, green, blue)
