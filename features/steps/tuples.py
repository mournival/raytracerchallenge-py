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


@then("{}.{} = {:g}")
def step_impl(context, name, field, val):
    """
    :param name: Tuple Name
    :param field: Tuple Field
    :param val: Field Value
    :type context: behave.runner.Context
    """
    assert (context.tuples[name].__getattribute__(field) == val)


@step("{} is a point")
def step_impl(context, name):
    """
    :param name: Tuple Name
    :type context: behave.runner.Context
    """
    print(context.tuples[name])
    assert (context.tuples[name].isPoint())


@step("{} is not a vector")
def step_impl(context, name):
    """
    :param name: Tuple Name
    :type context: behave.runner.Context
    """
    assert (~context.tuples[name].isVector())


@step("{} is not a point")
def step_impl(context, name):
    """
    :param name: Tuple Name
    :type context: behave.runner.Context
    """
    assert (~context.tuples[name].isPoint())


@step("{} is a vector")
def step_impl(context, name):
    """
    :param name: Tuple Name
    :type context: behave.runner.Context
    """
    assert (context.tuples[name].isVector())


@given("{} ← point({:g}, {:g}, {:g})")
def step_impl(context, name, x, y, z):
    """
    :param name: Point Name
    :param x:
    :param y:
    :param z:
    :param w:
    :type context: behave.runner.Context    """
    context.tuples[name] = point(x, y, z)


@then("{:w} = tuple({:g}, {:g}, {:g}, {:g})")
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


@given("{} ← vector({:g}, {:g}, {:g})")
def step_impl(context, name, x, y, z):
    """
    :param name: Point Name
    :param x:
    :param y:
    :param z:
    :param w:
    :type context: behave.runner.Context    """
    context.tuples[name] = vector(x, y, z)


@then("{:w} + {:w} = tuple({:g}, {:g}, {:g}, {:g})")
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
