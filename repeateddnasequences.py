d = {}
rvd = []


def findRepeatedDnaSequences(s):
    i = 0
    while len(s) - i >= 10:
        sequence = s[i:i + 10]
        if not d.__contains__(sequence):
            d[sequence] = ""
        elif not rvd.__contains__(sequence):
            rvd.append(sequence)
        i += 1
    return rvd


s = input()
print(findRepeatedDnaSequences(s))
