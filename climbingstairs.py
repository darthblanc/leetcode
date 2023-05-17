d = {}


def climbstairs(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    if not d.__contains__(n):
        d[n] = climbstairs(n - 1) + climbstairs(n - 2)

    return d[n]


m = int(input())
print(climbstairs(m))
