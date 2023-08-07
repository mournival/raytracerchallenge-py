from collections import namedtuple

from behave import *

from features.tuple import Tuple

use_step_matcher("re")


@given("a ← tuple\(4\.3, -4\.2, 3\.1, 1\.0\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.tuples['a'] = Tuple(4.3, -4.2, 3.1, 1.0)


@then("a\.x = 4\.3")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert(context.tuples['a'].x == 4.3)


@step("a\.y = -4\.2")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert(context.tuples['a'].y == -4.2)


@step("a\.z = 3\.1")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert(context.tuples['a'].z == 3.1)


@step("a\.w = 1\.0")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert(context.tuples['a'].w == 1.0)


@step("a is a point")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert(context.tuples['a'].isPoint())


@step("a is not a vector")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert(context.tuples['a'].isVector())
