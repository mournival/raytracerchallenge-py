from behave import then, step

from features.environment import assert_equal, register_custom_parsers
from tuple import vector3, point

register_custom_parsers()


@then("{:id} is nothing")
def step_item_is_none(context, name):
    assert context.scenario_vars[name] is None, f"Actual {context.scenario_vars[name] = }, expected None"


@step("{:id}.count = {:rn}")
def step_count_is(context, xs, expected):
    actual = context.scenario_vars[xs]
    assert len(actual) == expected, f"{ actual = } expected is not {expected}"


@then("{:id}.normalv = vector({:rns})")
def step_normalv_equals_id(context, a, s):
    assert_equal(context.scenario_vars[a].normalv, vector3(*s))


@then("{:id}.object = {:id}")
def step_object_equals_id(context, a, s):
    assert_equal(context.scenario_vars[a].object, context.scenario_vars[s])


@then("{:id}.object = {:id}.object")
def step_object_equals_val(context, a, s):
    assert_equal(context.scenario_vars[a].object, context.scenario_vars[s].object)


@then("{:id}[{:rn}].object = {:id}")
def step_object_i_equals_id(context, a, i, b):
    assert_equal(context.scenario_vars[a][i].object, context.scenario_vars[b])


@then("{:id}.point = point({:rns})")
def step_point_equals_id(context, a, s):
    assert_equal(context.scenario_vars[a].point, point(*s))


@then("{:id}.t = {:rn}")
def step_t_equals_val(context, a, t):
    assert_equal(context.scenario_vars[a].t, t)


@then("{:id}[{:rn}].t = {:rn}")
def step_t_i_equals_val(context, a, i, t):
    assert_equal(context.scenario_vars[a][i].t, t)


@then("{:id}.t = {:id}.t")
def step_a_t_equals_b_t(context, a, b):
    assert_equal(context.scenario_vars[a].t, context.scenario_vars[b].t)


@then("{:id}.inside = false")
def step_inside_equals_false(context, name):
    assert_equal(context.scenario_vars[name].inside, False)


@then("{:id}.inside = true")
def step_inside_equals_true(context, name):
    assert_equal(context.scenario_vars[name].inside, True)


@then("{:id}.eyev = vector({:rns})")
def step_eyev_equals_v(context, name, args):
    assert_equal(context.scenario_vars[name].eyev, vector3(*args))
