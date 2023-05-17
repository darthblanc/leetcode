d = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


def myAtoi(s):
    rv = ""
    cons = 1
    for c in s:
        if not d.__contains__(c) and c != " ":
            break
        if c == " ":
            continue
        if c == "-":
            cons *= -1
        if d.__contains__(c):
            rv += c

    rv = int(rv) * cons
    return rv


print(myAtoi("42"))
print(myAtoi("-42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
