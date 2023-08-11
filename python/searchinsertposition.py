def searchInsert(nums, target):
    if nums.__contains__(target):
        return nums.index(target)

    nums.append(target)
    nums.sort()
    return nums.index(target)


# redo this problem
print(searchInsert(nums=[1, 3, 5, 6], target=5))
print(searchInsert(nums=[1, 3, 5, 6], target=2))
print(searchInsert([1, 3, 5, 6], target=7))
