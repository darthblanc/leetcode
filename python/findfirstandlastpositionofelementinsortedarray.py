def searchRange(nums, target):
    if not nums.__contains__(target):
        return [-1, -1]

    d = {}
    start = 0
    for num in nums:
        if d.__contains__(num):
            continue
        count = nums.count(num)
        start += count
        d[num] = count
        if num == target:
            return [start - count, start - 1]


print(searchRange([5, 7, 7, 8, 8, 10], 8))
print(searchRange([5, 7, 7, 8, 8, 10], 6))
print(searchRange([], 0))
