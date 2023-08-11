import math


def divide(dividend, divisor):
    cons = 1
    if dividend == 0:
        return 0
    if dividend == 1:
        return 0
    if divisor == 1:
        return dividend
    if dividend < 0 < divisor or dividend > 0 > divisor:
        cons = -1
    dividend = math.fabs(dividend)
    divisor = math.fabs(divisor)
    rv = math.log(dividend, 10) - math.log(divisor, 10)
    return math.trunc(cons * (10 ** rv))


print(divide(10, 3))
print(divide(7, -3))
