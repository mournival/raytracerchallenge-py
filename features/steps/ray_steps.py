from behave import use_step_matcher, then, when, register_type

from features.environment import parse_ratio, parse_operation, parse_id, assert_equal

use_step_matcher("parse")
register_type(id=parse_id)
register_type(rn=parse_ratio)
register_type(op=parse_operation)


@when("{:id} ← {:op}({:id}, {:id})")
def step_tuple_create_derived(context, r, operation, a, b):
    context.scenario_vars[r] = operation(context.scenario_vars[a], context.scenario_vars[b])


@then("{:id}.origin = {:id}")
def step_tuple_field_equals(context, name, expected):
    assert_equal(context.scenario_vars[name].origin, context.scenario_vars[expected])


@then("{:id}.direction = {:id}")
def step_tuple_field_equals(context, name, expected):
    assert_equal(context.scenario_vars[name].direction, context.scenario_vars[expected])
