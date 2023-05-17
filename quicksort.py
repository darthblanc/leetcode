def myquicksort(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr

    pivot = arr[0]

    larr = []
    earr = []
    garr = []

    for x in arr:
        if x < pivot:
            larr.append(x)
        if x == pivot:
            earr.append(x)
        if x > pivot:
            garr.append(x)
    return myquicksort(larr) + earr + myquicksort(garr)


nums = [2, 0, 2, 1, 1, 0]
print(myquicksort(nums))

