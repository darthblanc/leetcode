from itertools import combinations


def subsets(nums):
    rv = []

    for i in range(len(nums) + 1):
        rv.append(list(combinations(nums, i)))

    r = []
    for i in range(len(rv)):
        for j in range(len(rv[i])):
            r.append(list(rv[i][j]))

    return r


print(subsets([1, 2, 3]))
print(subsets([0]))
