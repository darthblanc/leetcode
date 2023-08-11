def groupAnagrams(strs):
    d = {}

    for s in strs:
        r = [c for c in s]
        r.sort()
        t = ""
        for x in r:
            t += x

        if d.__contains__(t):
            d[t].append(s)

        else:
            d[t] = [s]

    rv = []

    for x in d:
        rv.append(d[x])

    return rv


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
