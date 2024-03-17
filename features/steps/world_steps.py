import numpy as np
from behave import given, when, then, step
from behave.model import Row

import material as mat
from color import color
from features.environment import assert_equal, method_mapping, operation_mapping, register_custom_parsers, \
    assert_approximately_equal
from intersect import EPSILON, intersection
from matrix import eye
from plane import Plane
from ray import lighting
from sphere import sphere
from tuple import z, point
from world import is_shadowed, World

register_custom_parsers()


@step("{:id} ← intersect_world({:id}, {:id})")
def step_create_intersect_world_ids(context, xs, wrld, ry):
    context.scenario_vars[xs] = context.scenario_vars[wrld].intersect(context.scenario_vars[ry])


@step("{:id} ← the first object in {:id}")
def step_first_object(context, shape, wrld):
    context.scenario_vars[shape] = context.scenario_vars[wrld].entities[0]


@step("{:id} ← the second object in {:id}")
def step_second_object(context, shape, wrld):
    context.scenario_vars[shape] = context.scenario_vars[wrld].entities[1]


@step("{:id} ← intersection({:rn}, {:id})")
def step_create_intersection(context, name, t, o):
    context.scenario_vars[name] = intersection(t, context.scenario_vars[o])


@when("{:id} ← canvas_to_ppm({:id})")
def step_canvas_create_ppm_string(context, ppm, c):
    context.scenario_vars[ppm] = context.scenario_vars[c].to_ppm()


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


@step("{:method}({:id}, {:id})")
def step_set_transform(context, method, s, t):
    context.scenario_vars[s] = method(context.scenario_vars[s], context.scenario_vars[t])


@step("{:method}({:id}, {:op}({:rns}))")
def step_set_transform_from_op(context, method, s, op, x):
    context.scenario_vars[s] = method(context.scenario_vars[s], op(*x))


@step("{:id} ← plane()")
def step_create_plane(context, name):
    context.scenario_vars[name] = Plane()


@step("{:id} ← lighting({:id}, {:id}, point({:rns}), {:id}, {:id}, false)")
def step_lighting(context, c1, m, light, p_params, eyev, normalv):
    context.scenario_vars[c1] = lighting(
        context.scenario_vars[m],
        context.scenario_vars[light],
        point(*p_params),
        context.scenario_vars[eyev],
        context.scenario_vars[normalv],
        False
    )


@given("{:id}.light ← {:op}({:op}({:rns}), {:op}({:rns}))")
def step_create_op2_with_op_op_vals(context, name, op1, op2, params2, op3, params3):
    context.scenario_vars[name] = World(op1(op2(*params2), op3(*params3)), context.scenario_vars[name].entities)


@step("{:id} is added to {:id}")
def step_add_entity(context, s, w):
    world = context.scenario_vars[w]
    entities = world.entities
    entities.append(context.scenario_vars[s])
    context.scenario_vars[w] = World(world.light, entities)


@when("write_pixel({:id}, {:rn}, {:rn}, {:id})")
def step_canvas_write_pixel(context, c, x, y, name):
    context.scenario_vars[c][x, y] = context.scenario_vars[name]


@when("every pixel of {:id} is set to color({:rns})")
def step_canvas_fill(context, c, ps):
    context.scenario_vars[c].fill(color(*ps))


@step("every pixel of {:id} is color({:rns})")
def step_canvas_pixels_are(context, c, ps):
    for p in context.scenario_vars[c].pixels():
        assert np.allclose(p, color(*ps)), f"every pixel of {c} is NOT color({ps})"


@then("pixel_at({:id}, {:rn}, {:rn}) = {:id}")
def step_canvas_pixel_at_from_id(context, c, x, y, name):
    assert np.allclose(context.scenario_vars[c][x, y],
                       context.scenario_vars[name]), f"pixel_at({c}, {x}, {y}) != {context.scenario_vars[c][x, y]}"


@then("pixel_at({:id}, {:rn}, {:rn}) = {:op}({:rns})")
def step_canvas_pixel_at_from_op(context, c, x, y, op, params):
    assert np.allclose(context.scenario_vars[c][x, y], op(*params),
                       rtol=0.0001), f"{context.scenario_vars[c][x, y]} != {op(*params)}"


@then("lines {:rn}-{:rn} of {:id} are")
def step_canvas_ppm_lines_are(context, a, b, ppm):
    actual = context.scenario_vars[ppm].splitlines()
    expected = context.text.splitlines()
    i = a - 1
    for r in expected[0:b - a + 1]:
        assert actual[i] == r, f"line {i} expected: '{r}', actual: '{actual[i]}'"
        i += 1


@then("{:id} ends with a newline character")
def step_canvas_ppm_end_newline(context, ppm):
    assert context.scenario_vars[ppm][-1] == '\n', f"{ppm} does not end with a newline character"


@step("{:id} has no light source")
def step_test_no_light_source(context, w):
    assert context.scenario_vars[w].light is None


@then("{:id} contains no objects")
def step_test_no_objects(context, w):
    assert_equal(len(context.scenario_vars[w].entities), 0)


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


@then("{:id}.over_point.z < -EPSILON/2")
def z_step_impl(context, comps):
    assert z(context.scenario_vars[comps].over_point) < EPSILON / 2


@then("{:id}.point.z > {:id}.over_point.z")
def z_compare_step_impl(context, a, b):
    assert z(context.scenario_vars[a].point) > z(context.scenario_vars[b].over_point)


@then("{:id}.height = {:rn}")
def step_height_equals_val(context, name, expected):
    assert_approximately_equal(context.scenario_vars[name].height, expected)


@then("{:id}.width = {:rn}")
def step_width_equals_val(context, name, expected):
    assert_approximately_equal(context.scenario_vars[name].width, expected)


@then("{:id}.field_of_view = {:rn}")
def step_field_of_view_equals_val(context, name, expected):
    assert_approximately_equal(context.scenario_vars[name].field_of_view, expected)


@then("{:id}.intensity = {:id}")
def step_intensity_equals_val(context, name, p):
    assert_approximately_equal(context.scenario_vars[name].intensity, context.scenario_vars[p])

@then("{:id}.light = {:id}")
def step_light_equals_val(context, w, p):
    actual = context.scenario_vars[w].light
    expected = context.scenario_vars[p]
    assert_equal(actual, expected)


@then("{:id}.position = {:id}")
def step_position_equals_val(context, name, p):
    assert_approximately_equal(context.scenario_vars[name].position, context.scenario_vars[p])
