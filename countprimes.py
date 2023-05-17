d = {}


def countPrimes(n):
    if n <= 2:
        return 0

    if not d.__contains__(n):
        for i in range(3, n):
            if n % i == 0:
                d[n] = 0 + countPrimes(n - 1)
                return d[n]
        d[n] = 1 + countPrimes(n - 1)

    return d[n]


print(countPrimes(10))
print("*******************")
print(countPrimes(0))
print(countPrimes(1))
print(countPrimes(4))
print(countPrimes(2))
print(countPrimes(499979))
