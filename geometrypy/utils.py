from math import fabs


def float_equal(f1, f2, precision=0.0001):
    return fabs(f1 - f2) <= precision
