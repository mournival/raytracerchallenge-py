from behave import *

from features.tuple import Tuple, point, vector

use_step_matcher("parse")


@given('{} ← tuple({:g}, {:g}, {:g}, {:g})')
def step_impl(context, a, x, y, z, w):
    """
    :param a: Tuple Name
    :param x:
    :param y:
    :param z:
    :param w:
    :type context: behave.runner.Context
    """
    context.tuples[a] = Tuple(x, y, z, w)


@then("{:S}.{:S} = {:g}")
def step_impl(context, name, field, val):
    """
    :param name: Tuple Name
    :param field: Tuple Field
    :param val: Field Value
    :type context: behave.runner.Context
    """
    assert (context.tuples[name].__getattribute__(field) == float(val))


@step("{:S} is a point")
def step_impl(context, name):
    """
    :param name: Tuple Name
    :type context: behave.runner.Context
    """
    print(context.tuples[name])
    assert (context.tuples[name].isPoint())


@step("{:S} is not a vector")
def step_impl(context, name):
    """
    :param name: Tuple Name
    :type context: behave.runner.Context
    """
    assert (~context.tuples[name].isVector())


@step("{:S} is not a point")
def step_impl(context, name):
    """
    :param name: Tuple Name
    :type context: behave.runner.Context
    """
    assert (~context.tuples[name].isPoint())


@step("{:S} is a vector")
def step_impl(context, name):
    """
    :param name: Tuple Name
    :type context: behave.runner.Context
    """
    assert (context.tuples[name].isVector())


@given("{:S} ← point({:g}, {:g}, {:g})")
def step_impl(context, name, x, y, z):
    """
    :param name: Point Name
    :param x:
    :param y:
    :param z:
    :type context: behave.runner.Context    """
    context.tuples[name] = point(x, y, z)


@then("{:S} = tuple({:g}, {:g}, {:g}, {:g})")
def step_impl(context, name, x, y, z, w):
    """
    :param name: Point Name
    :param x:
    :param y:
    :param z:
    :param w:
    :type context: behave.runner.Context
    """
    expected = Tuple(x, y, z, w)
    actual = context.tuples[name]
    assert (actual == expected)


@given("{:S} ← vector({:g}, {:g}, {:g})")
def step_impl(context, name, x, y, z):
    """
    :param name: Point Name
    :param x:
    :param y:
    :param z:
    :type context: behave.runner.Context    """
    context.tuples[name] = vector(x, y, z)


@then("{:S} + {:S} = tuple({:g}, {:g}, {:g}, {:g})")
def step_impl(context, a, b, x, y, z, w):
    """
    :param a: Tuple Name
    :param b: Tuple Name
    :param x:
    :param y:
    :param z:
    :param w:
    :type context: behave.runner.Context
    """
    expected = Tuple(x, y, z, w)
    actual = context.tuples[a] + context.tuples[b]
    print(actual)
    assert (actual == expected)


@then("{} - {} = vector({:g}, {:g}, {:g})")
def step_impl(context, a, b, x, y, z):
    """
    :param a: Tuple Name
    :param b: Tuple Name
    :param x:
    :param y:
    :param z:
    :type context: behave.runner.Context
    """
    expected = vector(x, y, z)
    actual = context.tuples[a] - context.tuples[b]
    print(actual)
    assert (actual == expected)


@then("{} - {} = point({:g}, {:g}, {:g})")
def step_impl(context, a, b, x, y, z):
    """
    :param a: Tuple Name
    :param b: Tuple Name
    :param x:
    :param y:
    :param z:
    :type context: behave.runner.Context
    """
    expected = point(x, y, z)
    actual = context.tuples[a] - context.tuples[b]
    print(actual)
    assert (actual == expected)