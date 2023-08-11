def removeDuplicates(nums):
    num_p = []

    for num in nums:
        if num_p.count(num) < 2:
            num_p.append(num)

    for i in range(len(num_p)):
        nums[i] = num_p[i]

    return len(num_p)


print(removeDuplicates(nums=[1, 1, 1, 2, 2, 3]))
print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
