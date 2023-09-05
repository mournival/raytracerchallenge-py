from behave import use_step_matcher, given, then, step, register_type

import matrix
from color import color
from features.environment import assert_equal, parse_user_g, parse_operation, assert_approximately_equal, parse_id, \
    parse_is_is_not, parse_field, parse_method, parse_matrix_name, create_table_from, assert_array_equal, \
    assert_array_approximately_equal, assert_array_not_equal
from tuple import is_point, is_vector

use_step_matcher("parse")
register_type(field=parse_field)
register_type(id=parse_id)
register_type(isnota=parse_is_is_not)
register_type(mn=parse_matrix_name)
register_type(mthd=parse_method)
register_type(op=parse_operation)
register_type(rn=parse_user_g)


@given("{:id} ← {:op}()")
def step_create_default(context, a, op):
    context.scenario_vars[a] = op()


@given("{:mn}")
def step_create__empty_n_m(context, name):
    context.scenario_vars[name] = create_table_from(context)


@step("{:id} ← {:op}({:rn})")
def step_create_op1_val(context, c, op, radians):
    context.scenario_vars[c] = op(radians)


@step("{:id} ← {:op}({:id})")
def step_create_op1_id(context, b, op, a):
    context.scenario_vars[b] = op(context.scenario_vars[a])


@step("{:id} ← {:op}({:rn}, {:id})")
def step_create_op2_val_id(context, name, dtype, t, o):
    context.scenario_vars[name] = dtype(t, context.scenario_vars[o])


@step("{:id} ← {:op}({:id}, {:id})")
def step_create_op2_ids(context, a, op, u, v):
    context.scenario_vars[a] = op(context.scenario_vars[u], context.scenario_vars[v])


@given("{:id} ← {:op}({:rn}, {:rn})")
def step_create_op2_val_val(context, c, op, h, w):
    context.scenario_vars[c] = op(h, w)


@given("{:id} ← {:op}({:rn}, {:rn}, {:rn})")
def step_create_op3_vals(context, name, dtype, x, y, z):
    context.scenario_vars[name] = dtype(x, y, z)


@given('{:id} ← {:op}({:rn}, {:rn}, {:rn}, {:rn})')
def step_create_op4(context, a, op, x, y, z, w):
    context.scenario_vars[a] = op(x, y, z, w)


@given("{:id} ← {:op}({:rn}, {:rn}, {:rn}) * {:op}({:rn})")
def step_create_op3_dot_op1(context, name, op1, x1, y1, z1, op2, rad):
    context.scenario_vars[name] = matrix.dot(op1(x1, y1, z1), op2(rad))


@given("{:id} ← {:op}({:op}({:rn}, {:rn}, {:rn}), {:op}({:rn}, {:rn}, {:rn}))")
def step_create_op2_with_op2_op2(context, name, op1, op2, x2, y2, z2, op3, x3, y3, z3):
    context.scenario_vars[name] = op1(op2(x2, y2, z2), op3(x3, y3, z3))


@step("{:id} ← {:op}({:id}, {:id}, {:id}, {:id})")
def step_create_op_4_ids(context, a, op, w, x, y, z):
    context.scenario_vars[a] = op(context.scenario_vars[w], context.scenario_vars[x], context.scenario_vars[y],
                                  context.scenario_vars[z])


@step("{:id} ← {:mthd}({:id}, {:op}({:rn}, {:rn}, {:rn}))")
def step_create_method_id_op3_vals(context, n, method, s, dtype, x, y, z):
    context.scenario_vars[n] = method(context.scenario_vars[s], dtype(x, y, z))


@step("{:id} ← {:id} * {:id}")
def step_create_product_ids(context, c, a, b):
    context.scenario_vars[c] = matrix.dot(context.scenario_vars[a], context.scenario_vars[b])


@step("{:id} ← {:id} * {:id} * {:id}")
def step_create_chained_product_ids(context, t, a, b, c):
    context.scenario_vars[t] = matrix.dot(matrix.dot(context.scenario_vars[a], context.scenario_vars[b]),
                                          context.scenario_vars[c])


@step("{:id} ← shearing({:rn}, {:rn}, {:rn}, {:rn}, {:rn}, {:rn})")
def step_create_shearing_vals(context, c, x_y, x_z, y_x, y_z, z_x, z_y):
    context.scenario_vars[c] = matrix.shearing(x_y, x_z, y_x, y_z, z_x, z_y)


@step("{:id} ← submatrix({:id}, {:rn}, {:rn})")
def step_create_submatrix(context, b, a, m, n):
    context.scenario_vars[b] = matrix.submatrix(context.scenario_vars[a], m, n)


@then("{:id} is nothing")
def step_item_is_none(context, name):
    assert context.scenario_vars[name] is None, f"Actual {context.scenario_vars[name] =}, expected None"


@then("{:id} {:isnota} point")
def step_test_is_point(context, name, is_or_not):
    assert_equal(is_point(context.scenario_vars[name]), is_or_not)


@then("{:id} {:isnota} vector")
def step_test_is_vector(context, name, is_or_not):
    assert_equal(is_vector(context.scenario_vars[name]), is_or_not)


@step("{:id} is invertible")
def step_is_invertible(context, a):
    assert (matrix.invertible(context.scenario_vars[a]))


@step("{:id} is not invertible")
def step_is_not_invertible(context, a):
    assert (not matrix.invertible(context.scenario_vars[a]))


@then("{:id}{:field} = {:op}({:rn}, {:rn}, {:rn})")
def step_field_equals_op3(context, name, field, op, x, y, z):
    assert_equal(field(context.scenario_vars[name]), op(x, y, z))


@then("{:id}[{:rn}]{:field} = {:rn}")
def step_array_element_field_equals_val(context, name, i, field, expected):
    assert_equal(field(context.scenario_vars[name][i]), expected)


@then("{:id}[{:rn}]{:field} = {:id}")
def step_array_element_field_equals_id(context, name, i, field, expected):
    assert_equal(field(context.scenario_vars[name][i]), context.scenario_vars[expected])


@then("{:id}{:field} = {:id}")
def step_field_equals_id(context, name, field, expected):
    assert_equal(field(context.scenario_vars[name]), context.scenario_vars[expected])


@then("{:id}{:field} = {:rn}")
def step_field_equals_val(context, name, field, expected):
    assert_equal(field(context.scenario_vars[name]), expected)


@then("-{:id} = {:op}({:rn}, {:rn}, {:rn}, {:rn})")
def step_negate_equals_op4_vals(context, name, op, x, y, z, w):
    assert_equal(-context.scenario_vars[name], op(x, y, z, w))


@then("{:id} = {:op}({:rn}, {:rn}, {:rn}, {:rn})")
def step_id_equals_op4_vals(context, name, op, x, y, z, w):
    assert_equal(context.scenario_vars[name], op(x, y, z, w))


@then("{:id} + {:id} = {:op}({:rn}, {:rn}, {:rn}, {:rn})")
def step_addition_equals_op4_vals(context, a, b, op, x, y, z, w):
    assert_equal(context.scenario_vars[a] + context.scenario_vars[b], op(x, y, z, w))


@then("{:id} - {:id} = {:op}({:rn}, {:rn}, {:rn})")
def step_subtraction_equals_op3_vals(context, a, b, dtype, x, y, z):
    expected = dtype(x, y, z)
    actual = context.scenario_vars[a] - context.scenario_vars[b]
    assert_approximately_equal(actual, expected)


@then("{:id} * {:rn} = {:op}({:rn}, {:rn}, {:rn}, {:rn})")
def step_scalar_multiplication_equals_op4_vals(context, a, c, op, x, y, z, w):
    assert_equal(context.scenario_vars[a] * c, op(x, y, z, w))


@then("{:id} / {:rn} = {:op}({:rn}, {:rn}, {:rn}, {:rn})")
def step_scalar_division_equals_op4_vals(context, a, c, op, x, y, z, w):
    assert_equal(context.scenario_vars[a] / c, op(x, y, z, w))


@then("{:op}({:id}) = {:rn}")
def step_op_id_equals_vals(context, op, a, expected):
    assert_approximately_equal(op(context.scenario_vars[a]), expected)


@then("{:op}({:id}) = approximately {:rn}")
def step_operation_approximately_equals_val(context, op, a, expected):
    assert_equal(op(context.scenario_vars[a]), expected)


@then("{:op}({:id}) = {:op}({:rn}, {:rn}, {:rn})")
def step_op1_id_equals_op3_val(context, op, v, dtype, x, y, z):
    assert_equal(op(context.scenario_vars[v]), dtype(x, y, z))


@then("{:op}({:id}) = approximately {:op}({:rn}, {:rn}, {:rn})")
def step_op1_id_approxoimatelu_equals_op3_val(context, op, v, dtype, x, y, z):
    assert_approximately_equal(op(context.scenario_vars[v]), dtype(x, y, z))


@then("{:op}({:id}, {:id}) = {:rn}")
def step_op2_ids_equals_val(context, op, a, b, expected):
    assert_equal(op(context.scenario_vars[a], context.scenario_vars[b]), expected)


@then("{:op}({:id}, {:id}) = {:op}({:rn}, {:rn}, {:rn})")
def step_op2_ids_equals_op3_vals(context, op1, a, b, op2, x, y, z):
    assert_equal(op1(context.scenario_vars[a], context.scenario_vars[b]), op2(x, y, z))


@then("{:id} = {:op}({:id})")
def step_id_equals_op1_id(context, a, op, b):
    assert_equal(context.scenario_vars[a], op(context.scenario_vars[b]))


@then("{:id} = {:op}({:rn}, {:rn}, {:rn})")
def step_id_equals_op3_vals(context, v, dtype, x, y, z):
    assert_approximately_equal(context.scenario_vars[v], dtype(x, y, z))


@then("{:id} = approximately {:op}({:rn}, {:rn}, {:rn})")
def step_id_approximately_equal_op3_vals(context, v, dtype, x, y, z):
    assert_approximately_equal(context.scenario_vars[v], dtype(x, y, z))


@then("{:id} + {:id} = {:op}({:rn}, {:rn}, {:rn})")
def step_addition_equals_op3_vals(context, a, b, op, r, g, bl):
    assert_equal(context.scenario_vars[a] + context.scenario_vars[b], op(r, g, bl))


@then("{:id} * {:rn} = {:op}({:rn}, {:rn}, {:rn})")
def step_scaling_equals_op3_vals(context, a, c, op, r, g, b):
    assert_equal(context.scenario_vars[a] * c, op(r, g, b))


@then("{:op}({:id}, {:rn}) = {:op}({:rn}, {:rn}, {:rn})")
def step_op2_id_val_equals_op3_vals(context, operation, r, t, dtype, x, y, z):
    assert_equal(operation(context.scenario_vars[r], t), dtype(x, y, z))


@then("{:id}[{:rn},{:rn}] = {:rn}")
def step_element_approximately_equals_val(context, name, r, c, expected):
    assert_approximately_equal(context.scenario_vars[name][r, c], expected)


@then("{:id} = {:id}")
def step_id_equals_id(context, a, b):
    assert_array_equal(context.scenario_vars[a], context.scenario_vars[b])


@then("{:id} * {:id} = {:id}")
def step_multiplication_equals_id(context, a, b, c):
    assert_array_equal(matrix.dot(context.scenario_vars[a], context.scenario_vars[b]), context.scenario_vars[c])


@then("{:id} * {:id} = {:op}({:rn}, {:rn}, {:rn})")
def step_point_multiplication_equals_op3_vals(context, a, b, dtype, x, y, z):
    if dtype == color:
        actual = context.scenario_vars[a] * context.scenario_vars[b]
    else:
        actual = matrix.dot(context.scenario_vars[a], context.scenario_vars[b])
    assert_array_approximately_equal(actual, dtype(x, y, z))


@then("{:id} != {:id}")
def step_not_equals(context, a, b):
    assert_array_not_equal(context.scenario_vars[a], context.scenario_vars[b])


@then("{:id} * {:id} is the following 4x4 matrix")
@then("{:id} * {:id} is the following 4x4 matrix:")
def step_multiplication_equals(context, a, b):
    assert_array_equal(matrix.dot(context.scenario_vars[a], context.scenario_vars[b]), create_table_from(context))


@then("{:id} is the following 4x4 matrix")
@then("{:id} is the following 4x4 matrix:")
def step_create_4x4_matrix(context, a):
    assert_array_approximately_equal(context.scenario_vars[a], create_table_from(context))


@then("{:op}({:id}) is the following matrix")
@then("{:op}({:id}) is the following matrix:")
@then("{:op}({:id}) is the following 4x4 matrix")
@then("{:op}({:id}) is the following 4x4 matrix:")
def step_marix_operations_approximately_equal(context, operation, a):
    assert_array_approximately_equal(operation(context.scenario_vars[a]), create_table_from(context))


@then("{:op}({:id}, {:rn}, {:rn}) = {:rn}")
def step_op3_id_equals_val(context, operation, a, r, c, expected):
    assert_approximately_equal(operation(context.scenario_vars[a], r, c), expected)


@then("{:id} * {:id} = {:op}({:rn}, {:rn}, {:rn}, {:rn})")
def step_dot_product_equals_op4_vals(context, a, b, op, x, y, z, w):
    assert_array_equal(matrix.dot(context.scenario_vars[a], context.scenario_vars[b]), op(x, y, z, w))


@then("submatrix({:id}, {:rn}, {:rn}) is the following {}x{} matrix")
@then("submatrix({:id}, {:rn}, {:rn}) is the following {}x{} matrix:")
def step_submatrix_equals(context, a, m, n, _m, _n):
    assert_array_equal(matrix.submatrix(context.scenario_vars[a], m, n), create_table_from(context))


@then("{:id} * {:op}({:id}) = {:id}")
def step_inverse_multiplication_equals(context, c, operation, b, a):
    actual = matrix.dot(context.scenario_vars[c], operation(context.scenario_vars[b]))
    assert_array_approximately_equal(actual, context.scenario_vars[a])
