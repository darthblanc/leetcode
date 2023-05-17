import math

d = {}


def trailingZeroes(n):
    if not d.__contains__(n):
        f = math.factorial(n)
        f = str(f)
        count = 0
        for c in range(len(f) - 1, -1, -1):
            if f[c] == '0':
                count += 1
            else:
                break
        d[n] = count
    return d[n]


print(trailingZeroes(3))
print(trailingZeroes(5))
print(trailingZeroes(0))
