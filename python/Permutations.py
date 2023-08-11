from itertools import permutations


def permute(nums):
    rv = list(permutations(nums, len(nums)))

    for i in range(len(rv)):
        rv[i] = list(rv[i])

    return rv


print(permute([1, 2, 3]))
print(permute([0, 1]))
print(permute([1]))
