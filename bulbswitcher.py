import math


def bulbSwitch(n):
    return int(math.sqrt(n))


print(bulbSwitch(3))
print(bulbSwitch(0))
print(bulbSwitch(1))
print(bulbSwitch(7))
print(bulbSwitch(99999))