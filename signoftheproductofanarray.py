def arraySign(nums):
    if nums.__contains__(0):
        return 0

    negative = len(list(filter(lambda x: x < 0, nums)))
    if negative % 2 == 1:
        return -1
    return 1


print(arraySign([-1, -2, -3, -4, 3, 2, 1]))
print(arraySign([1, 5, 0, 2, -3]))
print(arraySign([-1, 1, -1, 1, -1]))
