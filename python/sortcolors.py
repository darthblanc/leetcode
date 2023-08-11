def sortColors(nums):
    red = nums.count(0)
    white = red + nums.count(1)
    blue = white + nums.count(2)

    for num in range(len(nums)):
        if num < red:
            print("red", num)
            nums[num] = 0
        elif white > num >= red:
            print("white", num)
            nums[num] = 1
        elif blue > num >= white:
            print("blue", num)
            nums[num] = 2
    return nums


arr = [2, 0, 2, 1, 1, 0]
# arr = [2, 0, 1]
print(sortColors(arr))
