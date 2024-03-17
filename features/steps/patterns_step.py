from behave import given, then

from features.environment import register_custom_parsers, assert_approximately_equal
from pattern import StripePattern
from tuple import point

register_custom_parsers()


@given("{:id} ← stripe_pattern({:id}, {:id})")
def step_create_strip_pattern_vals(context, c, a, b):
    context.scenario_vars[c] = StripePattern(context.scenario_vars[a], context.scenario_vars[b])


@then("stripe_at({:id}, point({:rns})) = {:id}")
def step_color_at_equals_val(context, pattern, params, c):
    actual = context.scenario_vars[pattern].color_at(point(*params))
    expected = context.scenario_vars[c]
    assert_approximately_equal(actual, expected), f"{ actual = }, expected {context.scenario_vars[c]})"
