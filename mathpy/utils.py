def float_equal(f1, f2, precision=4):
    pre = 10 ** (-precision)

    return abs(f1 - f2) <= pre
