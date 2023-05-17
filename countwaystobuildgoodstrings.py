import math

d = {}


def countHelper(s, num, zero, one):
    if len(s) == num:
        return 1
    elif len(s) > num:
        return 0
    elif not d.__contains__((s, num, zero, num)):
        d[(s, num, zero, one)] = (countHelper(s + ("0" * zero), num, zero, one) + countHelper(s + ("1" * one), num,
                                                                                              zero,
                                                                                              one)) % (10 ** 9 + 7)
    return d[(s, num, zero, one)]


def countGoodStrings(low, high, zero, one):
    count = 0
    for num in range(low, high + 1):
        count += countHelper("", num, zero, one)
    return count


print(countGoodStrings(2, 3, 1, 2))
print(countGoodStrings(3, 3, 1, 1))
print(d)
print(countGoodStrings(200, 200, 10, 1))
