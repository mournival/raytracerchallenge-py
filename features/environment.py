from behave import fixture, use_fixture


def before_feature(context, feature):
    context.tuples = dict()