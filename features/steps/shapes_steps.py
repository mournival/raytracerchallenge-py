from behave import given, step, then

import matrix
from features.environment import register_custom_parsers, assert_equal, assert_approximately_equal
from tuple import point

register_custom_parsers()


@given("{:id} ← {:op}({:rns}) * {:op}({:rn})")
def step_create_op_dot_op1(context, name, op1, params, op2, rad):
    context.scenario_vars[name] = matrix.dot(op1(*params), op2(rad))


@step("{:id} ← intersect({:id}, {:id})")
def step_create_method_intersect_vals(context, n, s, p):
    context.scenario_vars[n] = context.scenario_vars[s].intersect(context.scenario_vars[p])


@step("{:id} ← normal_at({:id}, {:op}({:rns}))")
def step_create_method_normal_at_vals(context, n, s, dtype, params):
    context.scenario_vars[n] = context.scenario_vars[s].normal_at(dtype(*params))


@step("{:id} ← {:id}.material")
def step_set_from_material(context, m, s):
    context.scenario_vars[m] = context.scenario_vars[s].material


@step("{:id}.material ← {:id}")
def step_set_material(context, s, m):
    context.scenario_vars[s] = context.scenario_vars[s].set_material(context.scenario_vars[m])


@step("{:id} ← local_normal_at({:id}, point({:rns}))")
def step_set_local_normal_at_var(context, a, p, params):
    context.scenario_vars[a] = context.scenario_vars[p].local_normal_at(point(*params))


@step("{:id} ← local_intersect({:id}, {:id})")
def step_set_local_intersect_method(context, xs, p, r):
    context.scenario_vars[xs] = context.scenario_vars[p].local_intersect(context.scenario_vars[r])


@then("{:id}.material = {:id}")
def step_material_equals_id(context, a, t):
    assert_equal(context.scenario_vars[a].material, context.scenario_vars[t])


@step("{:id}.saved_ray.origin = {:op}({:rns})")
def step_origin_equals_op3(context, name, op, params):
    assert_equal(context.scenario_vars[name].saved_ray.origin, op(*params))


@then("{:id}.transform = {:id}")
def step_transform_equals_id(context, a, t):
    assert_approximately_equal(context.scenario_vars[a].transform, context.scenario_vars[t])


@then("{:id}.transform = {:op}({:rns})")
def step_diffuse_equals_val(context, a, op, params):
    assert_approximately_equal(context.scenario_vars[a].transform, op(*params))


@step("{:id}.saved_ray.direction = {:op}({:rns})")
def step_field_direction_op3(context, name, op, params):
    assert_equal(context.scenario_vars[name].saved_ray.direction, op(*params))


@then("{:id}.parent is nothing")
def step_parent_is_none(context, name):
    assert context.scenario_vars[name].parent is None, f"Actual {context.scenario_vars[name] = }, expected None"


@step("{:id} is empty")
def step_is_empty(context, a):
    assert len(context.scenario_vars[a]) == 0, f"{context.scenario_vars[a] = } expected is not empty"
