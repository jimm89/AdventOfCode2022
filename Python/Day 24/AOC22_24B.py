import sys, copy, re
from collections import defaultdict as dd
from math import gcd
import heapq as h
read = sys.stdin.read
f = open("AOC22_24A_in.txt")

a = [list(x) for x in f.read().split('\n')]

source = a[0].index('.')
sink = a[-1].index('.')

global n, m, LCM, inf
n = len(a)
m = len(a[0])
inf = 10**10
LCM = (n - 2) * (m - 2) // gcd(n - 2, m - 2)

dx = [0, 1, 0, -1, 0]
dy = [1, 0, -1, 0, 0]

b = [set() for _ in range(LCM)]

for i in range(n):
    for j in range(m):
        if a[i][j] == '>':
            b[0].add((i, j, 0))
        elif a[i][j] == 'v':
            b[0].add((i, j, 1))
        elif a[i][j] == '<':
            b[0].add((i, j, 2))
        elif a[i][j] == '^':
            b[0].add((i, j, 3))
        if a[i][j] != '#':
            a[i][j] = '.'

for t in range(LCM - 1):
    for x, y, z in b[t]:
        new_x = (x - 1 + dx[z]) % (n - 2) + 1
        new_y = (y - 1 + dy[z]) % (m - 2) + 1
        b[t + 1].add((new_x, new_y, z))

"""
    shortest path from source to sink at time 0
    repeats itself every 300 moves
    dp[t][x][y] = shortest time if I'm currently at pos x, y and the time mod LCM is t
"""
            
def get_(start_t, start):
    global n, m, LCM
    dp = [[[inf for y in range(m)] for x in range(n)] for t in range(LCM)]
    source = (0, a[0].index('.'))
    sink = (-1, a[-1].index('.'))
    if not start:
        source, sink = sink, source

    dp[start_t % LCM][source[0]][source[1]] = start_t

    q = [(start_t, start_t % LCM, source[0], source[1])]


    while q:
        d, t, x, y = h.heappop(q)
        if dp[t][x][y] != d:
            continue
        for k in range(5):
            xx = (x + dx[k]) % n
            yy = (y + dy[k]) % m
            if any([(xx, yy, zz) in b[(t + 1) % LCM] for zz in range(4)]):
                continue
            if a[xx][yy] != '#' and dp[(t + 1) % LCM][xx][yy] > d + 1:
                dp[(t + 1) % LCM][xx][yy] = d + 1
                h.heappush(q, (d + 1, (t + 1) % LCM, xx, yy))

    ret = 10**10
    for t in range(LCM):
        ret = min(ret, dp[t][sink[0]][sink[1]])
    
    return ret

ans = 0
flag = False
for _ in range(3):
    flag ^= True
    ans = get_(ans, flag)

print(ans)