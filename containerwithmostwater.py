import math


def maxArea(height):
    i = 0
    j = len(height) - 1
    area = 0
    while i <= j:
        breadth = min(height[i], height[j])
        length = int(math.fabs(j - i))
        contender = breadth * length
        if contender > area:
            area = contender
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))
