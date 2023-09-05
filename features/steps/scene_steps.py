import numpy as np
from behave import use_step_matcher, when, then, step, register_type

from color import color
from features.environment import parse_id, parse_operation, parse_user_g
from sphere import set_transform

use_step_matcher("parse")
register_type(id=parse_id)
register_type(op=parse_operation)
register_type(rn=parse_user_g)


@step("every pixel of {:id} is color({:rn}, {:rn}, {:rn})")
def step_canvas_pixels_are(context, c, r, g, b):
    for p in context.scenario_vars[c].pixels():
        assert np.allclose(p, color(r, g, b)), f"every pixel of {c} is NOT color({r}, {g}, {b})"


@when("write_pixel({:id}, {:rn}, {:rn}, {:id})")
def step_canvas_write_pixel(context, c, x, y, name):
    context.scenario_vars[c][x, y] = context.scenario_vars[name]


@then("pixel_at({:id}, {:rn}, {:rn}) = {:id}")
def step_canvas_pixel_at(context, c, x, y, name):
    assert np.allclose(context.scenario_vars[c][x, y],
                       context.scenario_vars[name]), f"pixel_at({c}, {x}, {y}) != {context.scenario_vars[c][x, y]}"


@when("{:id} ← canvas_to_ppm({:id})")
def step_canvas_create_ppm_string(context, ppm, c):
    context.scenario_vars[ppm] = context.scenario_vars[c].to_ppm()


@then("lines {:rn}-{:rn} of {:id} are")
def step_canvas_ppm_lines_are(context, a, b, ppm):
    actual = context.scenario_vars[ppm].splitlines()
    expected = context.text.splitlines()
    i = a - 1
    for r in expected[0:b - a + 1]:
        assert actual[i] == r, f"line {i} expected: '{r}', actual: '{actual[i]}'"
        i += 1


@when("every pixel of {:id} is set to color({:rn}, {:rn}, {:rn})")
def step_canvas_fill(context, c, r, g, b):
    context.scenario_vars[c].fill(color(r, g, b))


@then("{:id} ends with a newline character")
def step_canvas_ppm_end_newline(context, ppm):
    assert context.scenario_vars[ppm][-1] == '\n', f"{ppm} does not end with a newline character"


@step("set_transform({:id}, {:id})")
def step_set_transform(context, s, t):
    context.scenario_vars[s] = set_transform(context.scenario_vars[s], context.scenario_vars[t])


@step("set_transform({:id}, {:op}({:rn}, {:rn}, {:rn}))")
def step_set_transform_from_op(context, s, op, x, y, z):
    context.scenario_vars[s] = set_transform(context.scenario_vars[s], op(x, y, z))
