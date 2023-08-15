from behave import use_step_matcher, given, when, then, step

from canvas import Canvas
from color import Color

use_step_matcher("parse")


@given("{:w} ← canvas({:d}, {:d})")
def step_canvas_create(context, c, h, w):
    context.globals[c] = Canvas(h, w)


@then("{:w}.width = {:g}")
def step_canvas_width_equals(context, name, expected):
    assert context.globals[name].__getattribute__("width") == expected, f"{name}.width = {expected}"


@then("{:w}.height = {:g}")
def step_canvas_height_equals(context, name, expected):
    assert context.globals[name].__getattribute__("height") == expected, f"{name}.height = {expected}"


@step("every pixel of {:w} is color({:g}, {:g}, {:g})")
def step_canvas_pixels_are(context, c, r, g, b):
    for p in context.globals[c].pixels():
        assert p == Color(r, g, b), f"every pixel of {c} is NOT color({r}, {g}, {b})"


@when("write_pixel({:w}, {:d}, {:d}, {:w})")
def step_canvas_write_pixel(context, c, x, y, name):
    context.globals[c][x, y] = context.tuples[name]


@then("pixel_at({:w}, {:d}, {:d}) = {:w}")
def step_canvas_pixel_at(context, c, x, y, name):
    assert context.globals[c][x, y] == context.tuples[name], f"pixel_at({c}, {x}, {y}) != {context.globals[c][x, y]}"


@when("{:w} ← canvas_to_ppm({:w})")
def step_canvas_create_ppm_string(context, ppm, c):
    context.globals[ppm] = context.globals[c].to_ppm()


@then("lines {:d}-{:d} of {:w} are")
def step_canvas_ppm_lines_are(context, a, b, ppm):
    actual = context.globals[ppm].splitlines()
    expected = context.text.splitlines()
    i = a - 1
    for r in expected[0:b - a + 1]:
        assert actual[i] == r, f"line {i} expected: '{r}', actual: '{actual[i]}'"
        i += 1


@when("every pixel of {:w} is set to color({:g}, {:g}, {:g})")
def step_canvas_fill(context, c, r, g, b):
    context.globals[c].fill(Color(r, g, b))


@then("{:w} ends with a newline character")
def step_canvas_ppm_end_newline(context, ppm):
    assert context.globals[ppm][-1] == '\n', f"{ppm} does not end with a newline character"
