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
    dist[j][j] = 0
    for x in inp[j][9:]:
        y = x[:-1] if x[-1] == ',' else x
        dist[j][idx[y]] = dist[idx[y]][j] = 1

"""
    We don't have to open a valve when we pass it
    Path is length 30
    Bitmask DP?
    Bitmask of length n
    1 means valve is open
    
    Need to compress indices now
"""

global ans
ans = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

N = n - val.count(0) + 1

VAL = []
nodes = []
start = -1

for j in range(n):
    if val[j] or idx['AA'] == j:
        if idx['AA'] == j:
            start = len(VAL)
        nodes.append(j)
        VAL.append(val[j])

DIST = [[0]*N for _ in range(N)]
for i in range(N):
    DIST[i][i] = 0
    for j in range(N):
        DIST[i][j] = dist[nodes[i]][nodes[j]]

T = 26
dp = [[[-100000000 for mask in range(1 << N)] for j in range(N)] for i in range(T + 1)]

for j in range(N):
    if DIST[start][j] + 1 > T:
        continue
    dp[DIST[start][j] + 1][j][1 << j] = 0

score = [0] * (1 << N)
for mask in range(1 << N):
    curr = 0
    for j in range(N):
        if (mask >> j) & 1:
            curr += VAL[j]
    score[mask] = curr


for i in range(T):
    for j in range(N):
        for mask in range(1 << N):
            dp[i + 1][j][mask] = max(dp[i + 1][j][mask], dp[i][j][mask] + score[mask])
            if not (mask >> j) & 1:
                continue
            for k in range(N):
                if not (mask >> k) & 1 and DIST[j][k] + i + 1 <= T:
                    dp[i + 1 + DIST[j][k]][k][mask | (1 << k)] = max(dp[i + 1 + DIST[j][k]][k][mask | (1 << k)], dp[i][j][mask] + score[mask] * (DIST[j][k] + 1))

for i in range(1 << N):
    for j in range(1 << N):
        if (i & j != j): # j has to be a submask of i
            continue
        a1 = a2 = 0
        for x in range(N):
            a1 = max(a1, dp[T][x][j]) # I pursue the subset represented by j
            a2 = max(a2, dp[T][x][(1 << N) - 1 - i]) # The elephant pursues the subset represented by the complement of i, which necessarily contains nothing that is in j
        ans = max(ans, a1 + a2)
        j = (j - 1) & i

print(ans)