def findDifference(nums1, nums2):
    answer1 = [nums for nums in nums1 if not nums2.__contains__(nums)]
    rv1 = []
    rv2 = []
    for x in answer1:
        if not rv1.__contains__(x):
            rv1.append(x)
    answer2 = [nums for nums in nums2 if not nums1.__contains__(nums)]
    for x in answer2:
        if not rv2.__contains__(x):
            rv2.append(x)

    return [rv1, rv2]


print(findDifference([1, 2, 3], [2, 4, 6]))
print(findDifference([1, 2, 3, 3], [1, 1, 2, 2]))
