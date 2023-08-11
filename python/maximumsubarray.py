import sys


def maxCross(nums, mid):
    left_sum = 0
    left_max = sys.maxsize * -1

    for i in range(mid, -1, -1):
        left_sum += nums[i]
        if left_sum > left_max:
            left_max = left_sum

    right_sum = 0
    right_max = sys.maxsize * -1

    for i in range(mid + 1, len(nums)):
        right_sum += nums[i]
        if right_sum > right_max:
            right_max = right_sum

    if left_max == sys.maxsize * -1:
        left_max = 0

    if right_max == sys.maxsize * -1:
        right_max = 0

    if left_max < 0:
        left_max = 0

    if right_max < 0:
        right_max = 0

    return right_max + left_max


def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]

    mid = len(nums) // 2
    print(mid)
    left = maxSubArray(nums[:mid])
    right = maxSubArray(nums[mid:])
    cross = maxCross(nums, mid)

    return max(left, right, cross)


# print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(maxSubArray([1]))
# print(maxSubArray([5, 4, -1, 7, 8]))
# print(maxSubArray([1, 2]))
# print(maxSubArray([1,2,-1]))
