d = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=',
     ']', '!', '>', ';', '?', '#', '$', ')', '/'}


def checkifpalindrome(r):
    for i in range(int(len(r) / 2)):
        if r[i] != r[len(r) - 1 - i]:
            return False
    return True


def isPalindrome(s):
    s = [c.lower() for c in s if not d.__contains__(c) and c != ' ']
    r = ""
    for x in s:
        r += x
    return checkifpalindrome(r)


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))