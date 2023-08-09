from behave import *

from canvas import Canvas
from color import Color

use_step_matcher("parse")


@given("{:w} ← canvas({:d}, {:d})")
def step_impl(context, c, h, w):
    context.canvases[c] = Canvas(h, w)


@then("{:w}.width = {:g}")
def step_impl(context, name, expected):
    assert (context.canvases[name].__getattribute__("width") == expected)


@then("{:w}.height = {:g}")
def step_impl(context, name, expected):
    assert (context.canvases[name].__getattribute__("height") == expected)


@step("every pixel of {:w} is color({:g}, {:g}, {:g})")
def step_impl(context, c, r, g, b):
    for p in context.canvases[c].pixels():
        assert (p == Color(r, g, b))


@when("write_pixel({:w}, {:d}, {:d}, {:w})")
def step_impl(context, c, x, y, name):
    context.canvases[c][x, y] = context.tuples[name]


@then("pixel_at({:w}, {:d}, {:d}) = {:w}")
def step_impl(context, c, x, y, name):
    assert (context.canvases[c][x,y] == context.tuples[name])
