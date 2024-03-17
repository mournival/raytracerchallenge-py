from behave import step, then

from color import color
from features.environment import assert_approximately_equal, register_custom_parsers
from pattern import StripePattern

register_custom_parsers()


@step("in_shadow ← true")
def step_create_true(context):
    context.scenario_vars["in_shadow"] = True


@step("{:id}.pattern ← stripe_pattern(color({:rns}), color({:rns}))")
def step_create_strpe_patter(context, c, a_params, b_params):
    context.scenario_vars[c] = context.scenario_vars[c].set_pattern(StripePattern(color(*a_params), color(*b_params)))


@step("{:id}.ambient ← {:rn}")
def step_set_ambient(context, m, value):
    context.scenario_vars[m] = context.scenario_vars[m].set_ambient(value)


@step("{:id}.color ← color({:rns})")
def step_set_color(context, m, value):
    context.scenario_vars[m] = context.scenario_vars[m].set_color(color(value))


@step("{:id}.diffuse ← {:rn}")
def step_set_diffuse(context, m, value):
    context.scenario_vars[m] = context.scenario_vars[m].set_diffuse(value)


@step("{:id}.specular ← {:rn}")
def step_set_specular(context, m, val):
    context.scenario_vars[m] = context.scenario_vars[m].set_specular(val)


@then("{:id}.ambient = {:rn}")
def step_ambient_equals_val(context, name, expected):
    assert_approximately_equal(context.scenario_vars[name].ambient, expected)


@then("{:id}.color = color({:rns})")
def step_color_equals_val(context, name, p):
    assert_approximately_equal(context.scenario_vars[name].color, color(*p))


@then("{:id}.diffuse = {:rn}")
def step_diffuse_equals_val(context, name, expected):
    assert_approximately_equal(context.scenario_vars[name].diffuse, expected)


@then("{:id}.shininess = {:rn}")
def step_shininess_equals_val(context, name, expected):
    assert_approximately_equal(context.scenario_vars[name].shininess, expected)


@then("{:id}.specular = {:rn}")
def step_specular_equals_val(context, name, expected):
    assert_approximately_equal(context.scenario_vars[name].specular, expected)
