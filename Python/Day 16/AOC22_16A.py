import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_16A_in.txt")

inp = [s.split() for s in f.read().split('\n')]

global n
n = len(inp)

big = 10**9

dist = [[big] * n for _ in range(n)]

val = [int(s[4].split('=')[-1][:-1]) for s in inp]

idx = dd(int)
for j in range(n):
    idx[inp[j][1]] = j

#print(idx)

for j in range(n):
    for x in inp[j][9:]:
        y = x[:-1] if x[-1] == ',' else x
        dist[j][idx[y]] = dist[idx[y]][j] = 1

"""
    We don't have to open a valve when we pass it
    Path is length 30
    Bitmask DP?
    Bitmask of length n
    1 means valve is open
"""

global ans
ans = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

def dfs(node, state, score, total, num_moves):
    global ans
    ans = max(ans, total + (30 - num_moves) * score)
    for j in range(n):
        if not (state >> j) & 1 and val[j] > 0:
            if dist[node][j] + 1 + num_moves <= 30:
                dfs(j, state | (1 << j), score + val[j], total + score * (dist[node][j] + 1), num_moves + dist[node][j] + 1)
    return

dfs(idx['AA'], 0, 0, 0, 0)

print(ans)