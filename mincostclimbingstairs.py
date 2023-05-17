import sys

t = [sys.maxsize]
d = {}


def minCostHelper(path, step, size, cost):
    if step >= size:
        p = path.split("-")
        p = [int(x) for x in p]
        cost_of_path = 0
        p = list(filter(lambda x: x < size, p))
        for x in p:
            cost_of_path += cost[x]
        if t[0] > cost_of_path:
            t[0] = cost_of_path

        return path
    if not d.__contains__(path):
        return minCostHelper(path + "-" + str(step + 1), step + 1, size, cost) + minCostHelper(
            path + "-" + str(step + 2),
            step + 2,
            size,
            cost)
    return d[path]


def minCostClimbingStairs(cost):
    zero_step = minCostHelper("0", 0, len(cost), cost)
    one_step = minCostHelper("1", 1, len(cost), cost)
    minimum = t[0]
    t[0] = sys.maxsize

    return minimum


print(minCostClimbingStairs([10, 15, 20]))
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
