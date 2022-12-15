import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_15A_in.txt")

inp = [line.split() for line in f.read().split('\n')]

s, b = [], []

for x in inp:
    s.append((int(x[2][2:-1]), int(x[3][2:-1])))
    b.append((int(x[-2][2:-1]), int(x[-1][2:])))

"""
grid too big to populate all

so we must consider, for sensor, its circle and how many points of said circle lie on the line y = 2000000
they map overlap too

its circle is actually a diamond and extends to every point with <= M, where M is the Manhattan distance
"""

LO, HI = [0, 4 * 10**6]
rngs = [[] for _ in range(HI - LO + 1)]

for i in range(len(s)):
    sx, sy = s[i]
    bx, by = b[i]
    d = abs(bx - sx) + abs(by - sy)
    # how many points on the row y = 2000000 have distance <= d?
    lo = sx - d
    hi = sx + d
    rngs[sy].append([lo, hi])
    y = sy - 1
    diff = 1
    while y >= LO:
        if lo + diff <= hi - diff:
            rngs[y].append([lo + diff, hi - diff])
        else:
            break
        y -= 1
        diff += 1
    y = sy + 1
    diff = 1
    while y <= HI:
        if lo + diff <= hi - diff:
            rngs[y].append([lo + diff, hi - diff])
        else:
            break
        y += 1
        diff += 1
    
        
for ii, rng in enumerate(rngs):
    rng.sort()
    rngs2 = []
    i = 0
    while i < len(rng):
        j = i
        mx = rng[j][1]
        while j + 1 < len(rng) and rng[j + 1][0] <= mx:
            j += 1
            mx = max(mx, rng[j][1])
        rngs2.append((rng[i][0], mx))
        i = j + 1
    
    y = ii
    
    if rngs2[0][0] > LO:
        x = rngs2[0][0] - 1
        print(x * HI + y)
        break

    if rngs2[-1][1] < HI:
        x = rngs2[-1][1] + 1
        print(x * HI + y)
        break

    if len(rngs2) == 2:
        x = rngs2[0][1] + 1
        print(x * HI + y)
        break

