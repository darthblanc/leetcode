def removeDuplicates(nums):
    num_p = []

    for num in nums:
        if not num_p.__contains__(num):
            num_p.append(num)

    for i in range(len(num_p)):
        nums[i] = num_p[i]

    return len(num_p)


print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
