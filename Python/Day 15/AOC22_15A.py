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

rngs = []
y = 2000000

for i in range(len(s)):
    sx, sy = s[i]
    bx, by = b[i]
    d = abs(bx - sx) + abs(by - sy)
    # how many points on the row y = 2000000 have distance <= d?
    curr = abs(y - sy)
    if curr > d:
        continue
    else:
        rem = d - curr
        lo = sx - rem
        hi = sx + rem
        rng = [lo, hi]
        if by != y:
            rngs.append([lo, hi])
        elif bx == lo == hi:
            continue
        elif bx == lo:
            rngs.append([lo + 1, hi])
        else:
            rngs.append([lo, hi - 1])

rngs.sort()
rngs2 = []
i = 0
ans = 0
while i < len(rngs):
    j = i
    mx = rngs[j][1]
    while j + 1 < len(rngs) and rngs[j + 1][0] <= mx:
        j += 1
        mx = max(mx, rngs[j][1])
    rngs2.append((rngs[i][0], mx))
    ans += mx + 1 - rngs[i][0]
    i = j + 1

print(ans)
        