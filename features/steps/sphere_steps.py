from behave import use_step_matcher, given, step, then, when, register_type

from features.environment import parse_ratio, parse_operation, parse_id, assert_equal, parse_field
from sphere import sphere, set_transform

use_step_matcher("parse")
register_type(field=parse_field)
register_type(id=parse_id)
register_type(rn=parse_ratio)
register_type(op=parse_operation)


@given("{:id} ← sphere()")
def step_matrix_create_transpose(context, a):
    context.scenario_vars[a] = sphere()


@step("{:id} ← {:op}({:id}, {:id})")
def step_tuple_create_derived(context, a, operation, u, v):
    context.scenario_vars[a] = operation(context.scenario_vars[u], context.scenario_vars[v])


@step("{:id} ← {:op}({:id}, {:id}, {:id}, {:id})")
def step_tuple_create_derived_tuple(context, a, operation, w, x, y, z):
    context.scenario_vars[a] = operation(context.scenario_vars[w], context.scenario_vars[x], context.scenario_vars[y],
                                         context.scenario_vars[z])


@then("{:id}[{:d}] = {:g}")
def step_matrix_equals(context, name, i, expected):
    assert_equal(context.scenario_vars[name][i], expected)


@when("set_transform({:id}, {:id})")
def step_impl(context, s, t):
    context.scenario_vars[s] = set_transform(context.scenario_vars[s], context.scenario_vars[t])


@when("set_transform({:id}, {:op}({:g}, {:g}, {:g}))")
def step_impl(context, s, op, x, y, z):
    context.scenario_vars[s] = set_transform(context.scenario_vars[s], op(x, y, z))
