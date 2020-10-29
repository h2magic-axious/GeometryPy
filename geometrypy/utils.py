from math import fabs, pow


def float_equal(f1, f2, precision=4):
    return fabs(f1 - f2) <= pow(10, -precision)
