import math


def getsum(a, b):
    rv = []
    for x in range(int(math.fabs(a))):
        rv.append(int(math.fabs(a) / a))
    for x in range(int(math.fabs(b))):
        rv.append(int(math.fabs(b) / b))

    return sum(rv)


print(getsum(1, 2))
print(getsum(2, 3))
print(getsum(-1, 1))
print(getsum(-12, -8))
