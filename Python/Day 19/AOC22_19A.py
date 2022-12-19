"""

    This was not my initial passing submission, however this version is more robust, albeit much slower

"""

import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_19A_in.txt")

inp = [z.split() for z in f.read().split('\n')]

def get_cost(x):
    cost = [[0] * 4 for _ in range(4)]
    cost[0][0] = int(x[6])
    cost[1][0] = int(x[12])
    cost[2][0] = int(x[18])
    cost[2][1] = int(x[21])
    cost[3][0] = int(x[27])
    cost[3][2] = int(x[30])
    return cost

def get_best(x, T):
    cost = get_cost(x)
    vals = set([((1, 0), (0, 0), (0, 0), (0, 0))])
    ans = 0
    for t in range(T):
        new_vals = set()
        best = 0
        max_poss = 0
        for val in vals:
            new_val = [[v[0], v[0] + v[1]] for v in val]
            new_val = tuple(list(map(tuple, new_val)))
            new_vals.add(new_val)
            best = max(best, val[-1][-1] + val[-1][0])
            max_poss = max(max_poss, val[-1][-1] + val[-1][0] * (T - 1 - t))
            bools = [
                val[0][0] < max(cost[1][0], cost[2][0], cost[3][0]), # try new ore only if can't make the others
                val[1][0] < cost[2][1], # try new clay only if can't make an obs
                val[2][0] < cost[3][2], # try new obs only if can't make a geode
                True
            ]
            for j in range(4):
                if not all([val[k][1] >= cost[j][k] for k in range(4)]): # do we meet all the cost requirements?
                    continue
                new_val = [[v[0], v[0] + v[1]] for v in val]
                if bools[j]:
                    new_val[j][0] += 1
                    for k in range(4):
                        new_val[k][1] -= cost[j][k]
                    new_val = tuple(list(map(tuple, new_val)))
                    new_vals.add(new_val)
        vals = set()
        ans = max(ans, best)
        for val in new_vals:
            if val[-1][-1] + val[-1][0] * (T - 1 - t) >= max_poss:
                vals.add(val)
    return ans

T = 24

ans = [get_best(x, T) * i for i, x in enumerate(inp, start = 1)]

print(sum(ans))

