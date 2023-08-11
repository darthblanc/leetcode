def removeElement(nums, val):
    i = len(nums) - 1

    while i >= 0:
        print(nums)
        if nums[i] == val:
            del nums[i]
        i -= 1

    return nums


print(removeElement([3, 2, 2, 3], 3))
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
