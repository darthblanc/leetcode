import re


def isMatch(s, p):
    x = re.match(p, s)
    if bool(x):
        x = x.span()
        return (x[1] - x[0]) == len(s)

    return False


print(isMatch(s="aa", p="a"))
print(isMatch(s="aa", p="a*"))
print(isMatch("ab", p=".*"))
print(isMatch("ab", ".*c"))