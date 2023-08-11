def lengthoflastword(s):
    t = s.split()
    print(t)
    return len(t[len(t) - 1])


s = input()
print(lengthoflastword(s))
