from behave import step

import matrix
from features.environment import assert_equal, register_custom_parsers, assert_approximately_equal

register_custom_parsers()


@step("hsize ← {:rn}")
def step_set_hsize(context, val):
    context.scenario_vars["hsize"] = val


@step("vsize ← {:rn}")
def step_set_vsize(context, val):
    context.scenario_vars["vsize"] = val


@step("field_of_view ← {:rn}")
def step_set_field_of_view(context, val):
    context.scenario_vars["field_of_view"] = val


@step("{:id} ← ray_for_pixel({:id}, {:rn}, {:rn})")
def step_create_ray_for_pixel(context, n, p, p_x, p_y):
    context.scenario_vars[n] = context.scenario_vars[p].ray_for_pixel(p_x, p_y)


@step("{:id}.transform ← {:op}({:rns}) * {:op}({:rns})")
def step_create_product_op_values(context, c, op1, params1, op2, params2):
    context.scenario_vars[c] = context.scenario_vars[c].set_transform(matrix.dot(op1(*params1), op2(*params2)))


@step("{:id}.transform ← {:op}({:ids})")
def step_create_transform_op_ids(context, c, op1, params1):
    context.scenario_vars[c] = context.scenario_vars[c].set_transform(
        op1(*[context.scenario_vars[a] for a in params1]))


@step("{:id}.hsize = {:rn}")
def step_create_hsize(context, c, val):
    assert_approximately_equal(context.scenario_vars[c].hsize, val), f"{c}.hsize = {val}"


@step("{:id}.pixel_size = {:rn}")
def step_create_pixel_size(context, c, val):
    assert_approximately_equal(context.scenario_vars[c].pixel_size, val), f"{c}.pixel_size = {val}"


@step("{:id}.vsize = {:rn}")
def step_create_vsize(context, c, val):
    assert_equal(context.scenario_vars[c].vsize, val), f"{c}.vsize = {val}"
