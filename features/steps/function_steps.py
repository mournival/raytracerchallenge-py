from behave import given, then, step

from features.environment import assert_equal, assert_approximately_equal, register_custom_parsers
from tuple import point

register_custom_parsers()


@step("{:id} ← {:op}()")
def step_create_default(context, a, op):
    context.scenario_vars[a] = op()


@step("{:id} ← {:op}({:ids})")
def step_create_op_ids(context, a, op, ids):
    context.scenario_vars[a] = op(*[context.scenario_vars[i] for i in ids])


@given("{:id} ← {:op}({:rns})")
def step_create_op_vals(context, c, op, params):
    context.scenario_vars[c] = op(*params)


@given("{:id} ← {:op}({:op}({:rns}), {:op}({:rns}))")
def step_create_op2_with_op_op(context, name, op1, op2, params2, op3, params3):
    context.scenario_vars[name] = op1(op2(*params2), op3(*params3))


@step("{:id} ← {:method}({:id}, {:id})")
def step_set_functional_method(context, a, method, o, b):
    context.scenario_vars[a] = method(context.scenario_vars[o], context.scenario_vars[b])


@step("{:id}.count = {:rn}")
def step_count_is(context, xs, expected):
    actual = context.scenario_vars[xs]
    assert len(actual) == expected, f"{ actual = } expected is not {expected}"


@then("{:id} = {:op}({:rns})")
def step_id_equals_op_vals(context, name, op, params):
    assert_approximately_equal(context.scenario_vars[name], op(*params))


@then("{:op}({:id}) = {:rn}")
def step_op_id_equals_vals(context, op, a, expected):
    assert_approximately_equal(op(context.scenario_vars[a]), expected)


@then("{:op}({:id}) = {:op}({:rns})")
def step_op1_id_equals_op3_val(context, op, v, dtype, params):
    assert_equal(op(context.scenario_vars[v]), dtype(*params))


@then("{:op}({:id}, {:id}) = {:rn}")
def step_op2_ids_equals_val(context, op, a, b, expected):
    assert_equal(op(context.scenario_vars[a], context.scenario_vars[b]), expected)


@then("{:op}({:id}, {:id}) = {:op}({:rns})")
def step_op2_ids_equals_op3_vals(context, op1, a, b, op2, params):
    assert_equal(op1(context.scenario_vars[a], context.scenario_vars[b]), op2(*params))


@then("{:id} = {:op}({:id})")
def step_id_equals_op1_id(context, a, op, b):
    assert_equal(context.scenario_vars[a], op(context.scenario_vars[b]))


@then("{:id} = {:op}()")
def step_id_equals_op0(context, a, op):
    assert_equal(context.scenario_vars[a], op())


@then("{:id} = approximately {:op}({:rns})")
def step_id_approximately_equal_op3_vals(context, v, dtype, params):
    assert_approximately_equal(context.scenario_vars[v], dtype(*params))


@then("{:id} + {:id} = {:op}({:rns})")
def step_addition_equals_op3_vals(context, a, b, op, params):
    assert_equal(context.scenario_vars[a] + context.scenario_vars[b], op(*params))


@then("position({:id}, {:rn}) = point({:rns})")
def step_op2_id_val_equals_op3_vals(context, r, t, params):
    assert_equal(context.scenario_vars[r].position(t), point(*params))


@then("{:id}[{:rn},{:rn}] = {:rn}")
def step_element_approximately_equals_val(context, name, r, c, expected):
    assert_approximately_equal(context.scenario_vars[name][r, c], expected)


@then("{:op}({:id}, {:rn}, {:rn}) = {:rn}")
def step_op3_id_equals_val(context, operation, a, r, c, expected):
    assert_approximately_equal(operation(context.scenario_vars[a], r, c), expected)
