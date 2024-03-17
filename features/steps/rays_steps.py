from behave import step

from features.environment import assert_approximately_equal, register_custom_parsers
from tuple import vector3, point

register_custom_parsers()


@step("{:id}.direction = {:id}")
def step_direction_equals_id(context, a, b):
    assert_approximately_equal(context.scenario_vars[a].direction, context.scenario_vars[b])

@step("{:id}.origin = {:id}")
def step_origin_equals_id(context, a, b):
    assert_approximately_equal(context.scenario_vars[a].origin, context.scenario_vars[b])
@step("{:id}.origin = point({:rns})")
def step_origin_equals_val(context, a, p):
    assert_approximately_equal(context.scenario_vars[a].origin, point(*p))


@step("{:id}.direction = vector({:rns})")
def step_direction_equals_val(context, a, p):
    assert_approximately_equal(context.scenario_vars[a].direction, vector3(*p))
