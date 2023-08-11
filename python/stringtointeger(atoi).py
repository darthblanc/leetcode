import re


def myAtoi(s):
    pref = ""

    for i, c in enumerate(s):
        if re.match("[-+]", c):
            if len(pref) == 0:
                pref += c
            else:
                if pref == "+" or pref == "-":
                    return 0
                break
        elif re.match("[0-9]", c):
            pref += c
        elif c == " " and len(pref) == 0:
            continue
        else:
            break

    if len(pref) == 0:
        return 0
    print(pref)
    pref = int(pref)
    if pref > (2 ** 31) - 1:
        return (2 ** 31) - 1
    elif pref < (2 ** 31) * -1:
        return (2 ** 31) * -1
    else:
        return pref


# print(myAtoi("42"))
# print(myAtoi("     -42"))
# print(myAtoi("4193 with words"))
# print(myAtoi("words and 987"))
# print(myAtoi("00000-42a1234"))
# print(myAtoi("21474836460"))
print(myAtoi("+-12"))
print(myAtoi("-+12"))