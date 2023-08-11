def addBinary(a, b):
    r = int(a) + int(b)
    r = str(r)
    x = [0] * (len(r) + 1)

    for i in range(len(x)):
        x[i - 1] += int(r[i]) % 1
        x[i] += int(int(r[i]) / 2)
    print(x)


print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
