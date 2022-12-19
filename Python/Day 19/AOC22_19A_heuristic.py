"""

    This heuristic is fast, worked for part A, but later proved invalid for part B

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
    def dfs(t, vals):
        if t == T:
            if vals[-1][-1] > best[0]:
                best[0] = vals[-1][-1]
            return
        for j in range(3, -1, -1):
            # can I buy a new type j
            new_vals = [[val[0], val[0] + val[1]] for val in vals]
            poss = all([vals[k][1] >= cost[j][k] for k in range(4)])
            if poss:
                for k in range(4):
                    new_vals[k][1] -= cost[j][k]
                new_vals[j][0] += 1
                dfs(t + 1, new_vals)
                # this crude assumption says that if you can build a geode robot or an obsidian robot, you definitely should
                if j >= 2:
                    break
        # this crude assumption says that if you have at least 4 ore, build a robot of some description
        if vals[0][1] < 4:
            new_vals = [[val[0], val[0] + val[1]] for val in vals]
            dfs(t + 1, new_vals)
        return
    
    best = [0]
    dfs(0, [[1, 0], [0, 0], [0, 0], [0, 0]])
    return best[0]

T = 24

ans = [get_best(x, T) * i for i, x in enumerate(inp, start = 1)]

print(sum(ans))

