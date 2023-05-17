d = {}


def tribonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if not d.__contains__(n):
        d[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

    return d[n]


print(tribonacci(4))
print(tribonacci(25))
