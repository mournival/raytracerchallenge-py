from behave import given, step, then

import matrix
from color import color
from features.environment import create_table_from, assert_array_approximately_equal, assert_array_equal, \
    register_custom_parsers, assert_array_not_equal

register_custom_parsers()


@given("{:mn}")
def step_create__empty_n_m(context, name):
    context.scenario_vars[name] = create_table_from(context)


@step("{:id} ← {:id} * {:id} * {:id}")
def step_create_chained_product_ids(context, t, a, b, c):
    context.scenario_vars[t] = matrix.dot(matrix.dot(context.scenario_vars[a], context.scenario_vars[b]),
                                          context.scenario_vars[c])


@step("{:id} ← {:id} * {:id}")
def step_create_product_ids(context, c, a, b):
    context.scenario_vars[c] = matrix.dot(context.scenario_vars[a], context.scenario_vars[b])


@step("{:id} ← submatrix({:id}, {:rn}, {:rn})")
def step_create_submatrix(context, b, a, m, n):
    context.scenario_vars[b] = matrix.submatrix(context.scenario_vars[a], m, n)


@step("{:id} is invertible")
def step_is_invertible(context, a):
    A = context.scenario_vars[a]
    assert (matrix.invertible(A)), f"{ A = } expected is invertible"


@step("{:id} is not invertible")
def step_is_not_invertible(context, a):
    A = context.scenario_vars[a]
    assert not matrix.invertible(A), f"{ A = }, expected is not invertible"


@then("{:id} * {:id} is the following 4x4 matrix")
@then("{:id} * {:id} is the following 4x4 matrix:")
def step_multiplication_equals(context, a, b):
    assert_array_equal(matrix.dot(context.scenario_vars[a], context.scenario_vars[b]), create_table_from(context))


@then("{:id} * {:id} = {:id}")
def step_multiplication_equals_id(context, a, b, c):
    assert_array_equal(matrix.dot(context.scenario_vars[a], context.scenario_vars[b]), context.scenario_vars[c])


@then("{:id} * {:id} = {:op}({:rns})")
def step_point_multiplication_equals_op3_vals(context, a, b, dtype, params):
    if dtype == color:
        actual = context.scenario_vars[a] * context.scenario_vars[b]
    else:
        actual = matrix.dot(context.scenario_vars[a], context.scenario_vars[b])
    assert_array_approximately_equal(actual, dtype(*params))


@then("{:id} is the following 4x4 matrix")
@then("{:id} is the following 4x4 matrix:")
def step_create_4x4_matrix(context, a):
    assert_array_approximately_equal(context.scenario_vars[a], create_table_from(context))


@then("{:op}({:id}) is the following matrix")
@then("{:op}({:id}) is the following matrix:")
@then("{:op}({:id}) is the following 4x4 matrix")
@then("{:op}({:id}) is the following 4x4 matrix:")
def step_matrix_operations_approximately_equal(context, operation, a):
    assert_array_approximately_equal(operation(context.scenario_vars[a]), create_table_from(context))


@then("submatrix({:id}, {:rn}, {:rn}) is the following {}x{} matrix")
@then("submatrix({:id}, {:rn}, {:rn}) is the following {}x{} matrix:")
def step_submatrix_equals(context, a, m, n, _m, _n):
    assert_array_equal(matrix.submatrix(context.scenario_vars[a], m, n), create_table_from(context))


@then("{:id} * {:op}({:id}) = {:id}")
def step_inverse_multiplication_equals(context, c, operation, b, a):
    actual = matrix.dot(context.scenario_vars[c], operation(context.scenario_vars[b]))
    assert_array_approximately_equal(actual, context.scenario_vars[a])


@then("{:id} = {:id}")
def step_id_equals_id(context, a, b):
    assert_array_equal(context.scenario_vars[a], context.scenario_vars[b])


@then("{:id} != {:id}")
def step_not_equals(context, a, b):
    assert_array_not_equal(context.scenario_vars[a], context.scenario_vars[b])
