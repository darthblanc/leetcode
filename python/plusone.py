def plusOne(digits):
    num = 0
    i = 1
    for d in digits:
        num += d * (10 ** (len(digits) - i))
        i += 1
    num += 1
    num = str(num)
    num.split()
    num = [int(x) for x in num]
    return num


print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([9]))
