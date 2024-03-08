from behave import use_step_matcher, given, then, step, register_type

import matrix
from color import color, blue, green, red
from features.environment import assert_equal, parse_user_g, parse_operation, assert_approximately_equal, parse_id, \
    parse_is_is_not, parse_field, parse_method, parse_matrix_name, create_table_from, assert_array_equal, \
    assert_array_approximately_equal, assert_array_not_equal, parse_id_many, parse_user_g_many
from intersect import intersection
from tuple import is_point, is_vector, w, z, y, x
from world import World

use_step_matcher("parse")
register_type(field=parse_field)
register_type(id=parse_id)
register_type(ids=parse_id_many)
register_type(isnota=parse_is_is_not)
register_type(mn=parse_matrix_name)
register_type(method=parse_method)
register_type(op=parse_operation)
register_type(rn=parse_user_g)
register_type(rns=parse_user_g_many)


@step("{:id} ← {:rn}")
def step_set_value(context, a, val):
    context.scenario_vars[a] = val


@step("{:id} ← true")
def step_create_true(context, a):
    context.scenario_vars[a] = True


@step("{:id} ← {:op}()")
def step_create_default(context, a, op):
    context.scenario_vars[a] = op()


@given("{:mn}")
def step_create__empty_n_m(context, name):
    context.scenario_vars[name] = create_table_from(context)


@step("{:id} ← intersection({:rn}, {:id})")
def step_create_intersection(context, name, t, o):
    context.scenario_vars[name] = intersection(t, context.scenario_vars[o])


@step("{:id} ← ray_for_pixel({:id}, {:rn}, {:rn})")
def step_create_ray_for_pixel(context, name, o, x, y):
    context.scenario_vars[name] = context.scenario_vars[o].ray_for_pixel(x, y)


@step("{:id} ← {:op}({:ids})")
def step_create_op_ids(context, a, op, ids):
    context.scenario_vars[a] = op(*[context.scenario_vars[i] for i in ids])


@step("{:id} ← intersect_world({:id}, {:id})")
def step_create_interect_world_ids(context, xs, w, r):
    context.scenario_vars[xs] = context.scenario_vars[w].intersect(context.scenario_vars[r])


@given("{:id} ← {:op}({:rns})")
def step_create_op_vals(context, c, op, params):
    context.scenario_vars[c] = op(*params)


@given("{:id} ← {:op}({:rns}) * {:op}({:rn})")
def step_create_op_dot_op1(context, name, op1, params, op2, rad):
    context.scenario_vars[name] = matrix.dot(op1(*params), op2(rad))


@given("{:id} ← {:op}({:op}({:rns}), {:op}({:rns}))")
def step_create_op2_with_op_op(context, name, op1, op2, params2, op3, params3):
    context.scenario_vars[name] = op1(op2(*params2), op3(*params3))


@step("{:id} ← intersect({:id}, {:id})")
def step_create_method_intersect_vals(context, n, s, p):
    context.scenario_vars[n] = context.scenario_vars[s].intersect(context.scenario_vars[p])


@step("{:id} ← normal_at({:id}, {:op}({:rns}))")
def step_create_method_normal_at_vals(context, n, s, dtype, params):
    context.scenario_vars[n] = context.scenario_vars[s].normal_at(dtype(*params))


@step("{:id} ← {:id} * {:id}")
def step_create_product_ids(context, c, a, b):
    context.scenario_vars[c] = matrix.dot(context.scenario_vars[a], context.scenario_vars[b])


@step("{:id}.hsize = {:rn}")
def step_create_hsize(context, c, val):
    assert_equal(context.scenario_vars[c].hsize, val), f"{c}.hsize = {val}"


@step("{:id}.vsize = {:rn}")
def step_create_vsize(context, c, val):
    assert_equal(context.scenario_vars[c].vsize, val), f"{c}.vsize = {val}"


@step("{:id}.transform ← {:op}({:rns}) * {:op}({:rns})")
def step_create_product_op_values(context, c, op1, params1, op2, params2):
    context.scenario_vars[c] = context.scenario_vars[c].set_transform(matrix.dot(op1(*params1), op2(*params2)))


@step("{:id}.transform ← {:op}({:ids})")
def step_create_transform_op_ids(context, c, op1, params1):
    context.scenario_vars[c] = context.scenario_vars[c].set_transform(op1(*[context.scenario_vars[a] for a in params1]))


@step("{:id} ← {:id} * {:id} * {:id}")
def step_create_chained_product_ids(context, t, a, b, c):
    context.scenario_vars[t] = matrix.dot(matrix.dot(context.scenario_vars[a], context.scenario_vars[b]),
                                          context.scenario_vars[c])


@step("{:id} ← {:id}.material")
def step_set_from_material(context, m, s):
    context.scenario_vars[m] = context.scenario_vars[s].material


@step("{:id}.ambient ← {:rn}")
def step_set_from_field(context, m, value):
    context.scenario_vars[m] = context.scenario_vars[m].set_ambient(value)


@step("{:id}.material ← {:id}")
def step_set_material_from_field(context, s, m):
    context.scenario_vars[s] = context.scenario_vars[s].set_material(context.scenario_vars[m])


@step("{:id} ← submatrix({:id}, {:rn}, {:rn})")
def step_create_submatrix(context, b, a, m, n):
    context.scenario_vars[b] = matrix.submatrix(context.scenario_vars[a], m, n)


@then("{:id} is nothing")
def step_item_is_none(context, name):
    assert context.scenario_vars[name] is None, f"Actual {context.scenario_vars[name] =}, expected None"


@then("{:id}.parent is nothing")
def step_parent_is_none(context, name):
    assert context.scenario_vars[name].parent is None, f"Actual {context.scenario_vars[name] =}, expected None"


@then("{:id} {:isnota} point")
def step_test_is_point(context, name, is_or_not):
    assert_equal(is_point(context.scenario_vars[name]),
                 is_or_not), f"{is_point(context.scenario_vars[name]) =}, expected {is_or_not} point"


@then("{:id} {:isnota} vector")
def step_test_is_vector(context, name, is_or_not):
    assert_equal(is_vector(context.scenario_vars[name]),
                 is_or_not), f"{is_vector(context.scenario_vars[name]) =}, expected {is_or_not} vector"


@step("{:id} is invertible")
def step_is_invertible(context, a):
    assert (matrix.invertible(context.scenario_vars[a])), f"{context.scenario_vars[a] = } expected is invertible"


@step("{:id} is not invertible")
def step_is_not_invertible(context, a):
    assert (
        not matrix.invertible(context.scenario_vars[a])), f"{context.scenario_vars[a] =}, expected is not invertible"


@step("{:id}{:field} = {:op}({:rns})")
def step_field_equals_op3(context, name, field, op, params):
    assert_equal(field(context.scenario_vars[name]),
                 op(*params)), f"{field(context.scenario_vars[name]) =}, expected {op}({params})"


@step("{:id}.saved_ray.origin = {:op}({:rns})")
def step_origin_equals_op3(context, name, op, params):
    assert_equal(context.scenario_vars[name].saved_ray.origin, op(*params))


@step("{:id}.saved_ray.direction = {:op}({:rns})")
def step_field_direction_op3(context, name, op, params):
    assert_equal(context.scenario_vars[name].saved_ray.direction, op(*params))


@then("{:id}[{:rn}]{:field} = {:rn}")
def step_array_element_field_equals_val(context, name, i, field, expected):
    assert_equal(field(context.scenario_vars[name][i]), expected)


@then("{:id}[{:rn}]{:field} = {:id}")
def step_array_element_field_equals_id(context, name, i, field, expected):
    assert_equal(field(context.scenario_vars[name][i]), context.scenario_vars[expected])


@then("{:id}{:field} = {:id}")
def step_field_equals_id(context, name, field, expected):
    assert_equal(field(context.scenario_vars[name]), context.scenario_vars[expected])


@then("{:id}{:field} = false")
def step_field_equals_false(context, name, field):
    assert_equal(field(context.scenario_vars[name]), False)


@then("{:id}{:field} = true")
def step_field_equals_true(context, name, field):
    assert_equal(field(context.scenario_vars[name]), True)


@then("{:id}{:field} = {:id}{:field}")
def step_field_equals_field(context, name, field, expected_name, expected_field):
    assert_equal(field(context.scenario_vars[name]), expected_field(context.scenario_vars[expected_name]))


@then("{:id}{:field} = {:rn}")
def step_field_equals_val(context, name, field, expected):
    assert_approximately_equal(field(context.scenario_vars[name]), expected)


@then("{:id}.ambient = {:rn}")
def step_ambient_equals_val(context, name, expected):
    assert_approximately_equal(context.scenario_vars[name].ambient, expected)


@then("{:id}.blue = {:rn}")
def step_blue_equals_val(context, name, expected):
    assert_approximately_equal(blue(context.scenario_vars[name]), expected)


@then("{:id}.green = {:rn}")
def step_green_equals_val(context, name, expected):
    assert_approximately_equal(green(context.scenario_vars[name]), expected)


@then("{:id}.red = {:rn}")
def step_red_equals_val(context, name, expected):
    assert_approximately_equal(red(context.scenario_vars[name]), expected)


@then("{:id}.w = {:rn}")
def step_w_equals_val(context, name, expected):
    assert_approximately_equal(w(context.scenario_vars[name]), expected)


@then("{:id}.x = {:rn}")
def step_x_equals_val(context, name, expected):
    assert_approximately_equal(x(context.scenario_vars[name]), expected)


@then("{:id}.y = {:rn}")
def step_y_equals_val(context, name, expected):
    assert_approximately_equal(y(context.scenario_vars[name]), expected)


@then("{:id}.z = {:rn}")
def step_z_equals_val(context, name, expected):
    assert_approximately_equal(z(context.scenario_vars[name]), expected)


@given("{:id}.light ← {:op}({:op}({:rns}), {:op}({:rns}))")
def step_create_op2_with_op_op_vals(context, name, op1, op2, params2, op3, params3):
    context.scenario_vars[name] = World(op1(op2(*params2), op3(*params3)), context.scenario_vars[name].entities)


@then("-{:id} = {:op}({:rns})")
def step_negate_equals_op4_vals(context, name, op, params):
    assert_equal(-context.scenario_vars[name], op(*params))


@then("{:id} = {:op}({:rns})")
def step_id_equals_op_vals(context, name, op, params):
    assert_approximately_equal(context.scenario_vars[name], op(*params))


@then("{:id} - {:id} = {:op}({:rn}, {:rn}, {:rn})")
def step_subtraction_equals_op3_vals(context, a, b, dtype, x, y, z):
    assert_approximately_equal(context.scenario_vars[a] - context.scenario_vars[b], dtype(x, y, z))


@then("{:id} * {:rn} = {:op}({:rns})")
def step_scalar_multiplication_equals_op4_vals(context, a, c, op, params):
    assert_equal(context.scenario_vars[a] * c, op(*params))


@then("{:id} / {:rn} = {:op}({:rns})")
def step_scalar_division_equals_op4_vals(context, a, c, op, params):
    assert_equal(context.scenario_vars[a] / c, op(*params))


@then("{:op}({:id}) = {:rn}")
def step_op_id_equals_vals(context, op, a, expected):
    assert_approximately_equal(op(context.scenario_vars[a]), expected)


@then("{:op}({:id}) = approximately {:rn}")
def step_operation_approximately_equals_val(context, op, a, expected):
    assert_equal(op(context.scenario_vars[a]), expected)


@then("{:op}({:id}) = {:op}({:rns})")
def step_op1_id_equals_op3_val(context, op, v, dtype, params):
    assert_equal(op(context.scenario_vars[v]), dtype(*params))


@then("{:op}({:id}) = approximately {:op}({:rns})")
def step_op1_id_approximate_equals_op3_val(context, op, v, dtype, params):
    assert_approximately_equal(op(context.scenario_vars[v]), dtype(*params))


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


@then("{:method}({:id}, {:rn}) = {:op}({:rns})")
def step_op2_id_val_equals_op3_vals(context, operation, r, t, dtype, params):
    assert_equal(operation(context.scenario_vars[r], t), dtype(*params))


@then("{:id}[{:rn},{:rn}] = {:rn}")
def step_element_approximately_equals_val(context, name, r, c, expected):
    assert_approximately_equal(context.scenario_vars[name][r, c], expected)


@then("{:id} = {:id}")
def step_id_equals_id(context, a, b):
    assert_array_equal(context.scenario_vars[a], context.scenario_vars[b])


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
def step_matrix_operations_approximately_equal(context, operation, a):
    assert_array_approximately_equal(operation(context.scenario_vars[a]), create_table_from(context))


@then("{:op}({:id}, {:rn}, {:rn}) = {:rn}")
def step_op3_id_equals_val(context, operation, a, r, c, expected):
    assert_approximately_equal(operation(context.scenario_vars[a], r, c), expected)


@then("submatrix({:id}, {:rn}, {:rn}) is the following {}x{} matrix")
@then("submatrix({:id}, {:rn}, {:rn}) is the following {}x{} matrix:")
def step_submatrix_equals(context, a, m, n, _m, _n):
    assert_array_equal(matrix.submatrix(context.scenario_vars[a], m, n), create_table_from(context))


@then("{:id} * {:op}({:id}) = {:id}")
def step_inverse_multiplication_equals(context, c, operation, b, a):
    actual = matrix.dot(context.scenario_vars[c], operation(context.scenario_vars[b]))
    assert_array_approximately_equal(actual, context.scenario_vars[a])


@step("{:id} ← {:method}({:id}, {:id})")
def step_set_functional_method(context, a, method, o, b):
    context.scenario_vars[a] = method(context.scenario_vars[o], context.scenario_vars[b])


@step("{:id} ← the first object in {:id}")
def step_first_object(context, shape, w):
    context.scenario_vars[shape] = context.scenario_vars[w].entities[0]


@step("{:id} ← the second object in {:id}")
def step_second_object(context, shape, w):
    context.scenario_vars[shape] = context.scenario_vars[w].entities[1]
