import math


def divide(dividend, divisor):
    if dividend == 0:
        return 0
    if dividend > 0 and divisor == 1:
        return dividend
    if dividend > 0 and divisor == -1:
        return dividend * -1
    if dividend < 0 and divisor == 1:
        return dividend
    if dividend < 0 and divisor == -1:
        return dividend * -1
    ogdividend = dividend
    ogdivisor = divisor
    dividend = math.fabs(dividend)
    divisor = math.fabs(divisor)
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    if ogdivisor * ogdividend < 0:
        return quotient * -1
    return quotient


f = int(input())
s = int(input())
print()
print(divide(f, s))
