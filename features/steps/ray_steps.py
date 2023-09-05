from behave import use_step_matcher, then, register_type

from features.environment import parse_user_g, parse_operation, parse_id, assert_equal

use_step_matcher("parse")
register_type(id=parse_id)
register_type(rn=parse_user_g)
register_type(op=parse_operation)


@then("{:op}({:id}, {:g}) = {:op}({:g}, {:g}, {:g})")
def step_binary_operations_equal(context, operation, r, t, dtype, x, y, z):
    assert_equal(operation(context.scenario_vars[r], t), dtype(x, y, z))
