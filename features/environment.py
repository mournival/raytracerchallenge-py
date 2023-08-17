import math
import re
from cmath import sqrt

from parse import with_pattern


def before_feature(context, feature):
    context.scenario_vars = dict()


def assert_equal(actual, expected):
    assert actual == expected, f"{actual} != {expected}"


def assert_approximately_equal(actual, expected):
    epsilon = 0.0001
    assert abs((actual - expected)) < epsilon, f"{actual} !~ {expected}"


@with_pattern(r'-?√?π?\d*\s*/\s*\d+|√\d+')
def parse_ratio(text):
    a = text
    m = re.match(r'^√(\d+)$', a)
    if m:
        return sqrt(int(m.groups()[0]))
    a = text
    m = re.match("^(-)?(√)?(\d+)/(\d+)$", a)
    if m:
        groups = m.groups()
        sign = -1 if groups[0] else 1
        numerator = sqrt(int(groups[2])) if groups[1] else int(groups[2])
        denominator = int(groups[3])
        return sign * numerator / denominator
    a = text
    m = re.match(r'π / (\d+)$', a)
    if m:
        return math.pi / int(m.groups()[0])
    raise Exception(f"Error parsing {text}")


@with_pattern(r'[a-z]+_[a-z]+')
def parse_id(text):
    return text


@with_pattern(r'\w+')
def parse_operation(text):
    if text == 'transpose':
        import matrix
        return matrix.transpose
    if text == 'inverse':
        import matrix
        return matrix.inverse
    if text == 'translation':
        import matrix
        return matrix.translation
    if text == 'scaling':
        import matrix
        return matrix.scaling
    if text == 'determinant':
        import matrix
        return matrix.det
    if text == 'cofactor':
        import matrix
        return matrix.cofactor
    if text == 'minor':
        import matrix
        return matrix.minor
    if text == 'normalize':
        from tuple import normalize
        return normalize
    if text == 'dot':
        from tuple import dot
        return dot
    if text == 'cross':
        from tuple import cross
        return cross
    if text == 'magnitude':
        from tuple import magnitude
        return magnitude
    if text == 'point':
        from tuple import point
        return point
    if text == 'vector':
        from tuple import vector
        return vector
    if text == 'color':
        from color import Color
        return Color
    raise NotImplementedError(f"{text}")


@with_pattern(r'the following (\dx\d )?matrix \w+:?')
def parse_matrix_name(text):
    m = re.match(r'the following \d?x?\d? ?matrix (\w):?', text)
    return m.groups()[0]
