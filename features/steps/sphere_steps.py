from behave import use_step_matcher, given, when, register_type

from features.environment import parse_ratio, parse_operation, parse_id, parse_field
from sphere import sphere, set_transform

use_step_matcher("parse")
register_type(field=parse_field)
register_type(id=parse_id)
register_type(rn=parse_ratio)
register_type(op=parse_operation)


@given("{:id} ← sphere()")
def step_matrix_create_transpose(context, a):
    context.scenario_vars[a] = sphere()


@when("set_transform({:id}, {:id})")
def step_set_transform(context, s, t):
    context.scenario_vars[s] = set_transform(context.scenario_vars[s], context.scenario_vars[t])


@when("set_transform({:id}, {:op}({:g}, {:g}, {:g}))")
def step_set_transform_from_op(context, s, op, x, y, z):
    context.scenario_vars[s] = set_transform(context.scenario_vars[s], op(x, y, z))
