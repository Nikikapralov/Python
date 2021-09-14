def power(base, exponent):
    assert int(exponent) == exponent
    if exponent == 1:
        return base
    return base * power(base, exponent - 1)

print(power(2, 3))