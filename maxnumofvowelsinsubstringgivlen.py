def maxVowels(s, k):
    mem = {}
    d = {"a", "e", "i", "o", "u"}
    i = 0
    maximum = 0
    while i < len(s) - k + 1:
        sub = s[i:i + k]
        if not mem.__contains__(sub):
            mem[sub] = ""
            print(sub)
            count = 0
            for x in sub:
                if d.__contains__(x):
                    count += 1
            if count > maximum:
                maximum = count
            i += 1
    return maximum


print(maxVowels("abciiidef", 3))
print(maxVowels("aeiou", 2))
print(maxVowels("leetcode", 3))
print(maxVowels("weallloveyou", 7))
