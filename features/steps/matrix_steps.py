from behave import *

use_step_matcher("parse")


@given("the following 4x4 matrix M:")
def step_impl(context):
    raise NotImplementedError('Urgh')


@then("M[0,0] = 1")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then M[0,0] = 1')