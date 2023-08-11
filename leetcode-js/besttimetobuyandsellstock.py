import sys


def find_max_cross(low, mid, high, prices):
    left_maximum = sys.maxsize * -1
    left_sum = 0

    for i in range(mid, low - 1, - 1):
        left_sum += prices[i]
        left_maximum = max(left_sum, left_maximum)

    right_maximum = sys.maxsize * -1
    right_sum = 0

    for i in range(mid + 1, high + 1):
        right_sum += prices[i]
        right_maximum = max(right_sum, right_maximum)

    return left_maximum + right_maximum


def find_max_subarray(low, high, prices):
    if low == high:
        return prices[low]

    else:
        mid = (high + low) // 2

        left = find_max_subarray(low, mid, prices)
        right = find_max_subarray(mid + 1, high, prices)
        cross = find_max_cross(low, mid, high, prices)

    if left >= right and left >= cross:
        return left
    elif right > left and right >= cross:
        return right
    else:
        return cross


def maxProfit(prices):
    net_prices = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
    print(net_prices)
    b = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            b = 1

    if b == 1:
        return find_max_subarray(0, len(net_prices) - 1, net_prices)

    return 0


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([2, 1, 4]))
