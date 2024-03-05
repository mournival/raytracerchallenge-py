import numpy as np
from behave import use_step_matcher, given, when, then, step, register_type
from behave.model import Row

import material as mat
from color import color
from features.environment import parse_id, parse_operation, parse_user_g, assert_equal, method_mapping, \
    operation_mapping
from intersect import EPSILON
from matrix import eye
from sphere import sphere
from tuple import z
from world import is_shadowed, World

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
def step_canvas_pixel_at_from_id(context, c, x, y, name):
    assert np.allclose(context.scenario_vars[c][x, y],
                       context.scenario_vars[name]), f"pixel_at({c}, {x}, {y}) != {context.scenario_vars[c][x, y]}"


@then("pixel_at({:id}, {:rn}, {:rn}) = {:op}({:rns})")
def step_canvas_pixel_at_from_op(context, c, x, y, op, params):
    assert np.allclose(context.scenario_vars[c][x, y], op(*params),
                       rtol=0.0001), f"{context.scenario_vars[c][x, y]} != {op(*params)}"


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


@step("{:method}({:id}, {:id})")
def step_set_transform(context, method, s, t):
    context.scenario_vars[s] = method(context.scenario_vars[s], context.scenario_vars[t])


@step("{:method}({:id}, {:op}({:rns}))")
def step_set_transform_from_op(context, method, s, op, x):
    context.scenario_vars[s] = method(context.scenario_vars[s], op(*x))


@step("{:id} has no light source")
def step_test_no_light_source(context, w):
    assert context.scenario_vars[w].light is None


@then("{:id} contains no objects")
def step_test_no_objects(context, w):
    assert_equal(len(context.scenario_vars[w].entities), 0)


@given("{:id} ← sphere() with")
@given("{:id} ← sphere() with:")
def step_create_entity(context, a):
    heading_row = Row(context.table.headings, context.table.headings)
    table_data = context.table.rows
    table_data.insert(0, heading_row)
    d = {
        'material': mat.material(),
        'transform': eye(4)
    }
    for test_cmd, args in table_data:
        if '.' in test_cmd:
            dtype, field = test_cmd.split('.')
            if '(' in args:
                args = [float(n) for n in (args.translate(str.maketrans('', '', '(),')).split(' '))]
            else:
                args = float(args)
            d[dtype] = method_mapping[test_cmd](d[dtype], args)
        elif 'transform' == test_cmd:
            op, field = args.split('(')
            args = [float(n) for n in (field.translate(str.maketrans('', '', '(),')).split(' '))]
            d[test_cmd] = np.matmul(operation_mapping[op](*args), d[test_cmd])

    context.scenario_vars[a] = sphere(transform_matrix=d['transform'], material=d['material'])


@step("{:id} contains {:id}")
def step_contains_entity(context, w, o):
    contains = False
    obj = context.scenario_vars[o]
    for e in context.scenario_vars[w].entities:
        if e == obj:
            contains = True
    assert contains


@then("is_shadowed({:id}, {:id}) is false")
def step_is_shadowed_false(context, w, p):
    assert not is_shadowed(context.scenario_vars[w], context.scenario_vars[p])


@then("is_shadowed({:id}, {:id}) is true")
def step_is_shadowed_true(context, w, p):
    assert is_shadowed(context.scenario_vars[w], context.scenario_vars[p])


@step("{:id} is added to {:id}")
def step_add_entity(context, s, w):
    world = context.scenario_vars[w]
    entities = world.entities
    entities.append(context.scenario_vars[s])
    context.scenario_vars[w] = World(world.light, entities)


@then("{:id}.over_point.z < -EPSILON/2")
def z_step_impl(context, comps):
    assert z(context.scenario_vars[comps].over_point) < EPSILON / 2


@then("{:id}.point.z > {:id}.over_point.z")
def z_compare_step_impl(context, a, b):
    assert z(context.scenario_vars[a].point) > z(context.scenario_vars[b].over_point)
