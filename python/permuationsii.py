from itertools import permutations


def permuteUnique(nums):
    rv = []

    nums = list(permutations(nums, len(nums)))

    d = set()

    for num in nums:
        if not d.__contains__(num):
            rv.append(list(num))
            d.add(num)
        else:
            continue

    return rv


print(permuteUnique([1, 1, 2]))
print(permuteUnique([1, 2, 3]))
