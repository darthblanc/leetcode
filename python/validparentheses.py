from collections import deque

opener = {"(": ")", "[": "]", "{": "}"}


def isValid(s):
    if len(s) == 0:
        return True

    if len(s) % 2 == 1:
        return False

    if s[-1] == "(" or s[-1] == "[" or s[-1] == "{":
        return False

    stack = []

    for p in s:
        if opener.__contains__(p):
            stack.append(p)
        else:
            if opener[stack[-1]] == p:
                stack.pop()
            else:
                return False

    if len(stack) > 0:
        return False

    return True


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("{[]}"))
print(isValid("(){}}{"))
print(isValid("{}{}()[]"))
print(isValid("(("))
