def findNthDigit(n):
    rv = [str(x) for x in range(n + 1)]
    s = ""
    for x in rv:
        s += x

    return int(s[n])


print(findNthDigit(3))
print(findNthDigit(11))
print(findNthDigit(10000000))