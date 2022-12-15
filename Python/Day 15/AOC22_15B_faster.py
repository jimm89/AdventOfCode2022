"""

This solution uses the fact that there is only one valid point in the entire range.
This point must therefore be exactly be d + 1 away from some sensor, where d is the distance from that sensor to its nearest beacon.
(Otherwise adjacent points would be valid too)

'Faster' is relative: on my machine this runs in:
    20 seconds on Python (41 for previous solution)
    0.5 seconds on Pypy (20 for previous solution)

"""

import sys, copy, re
import time

start_time = time.time()
def TIME_(): print(time.time()-start_time)

from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_15A_in.txt")

inp = [line.split() for line in f.read().split('\n')]

global n
n = len(inp)
s, b = [], []

for x in inp:
    s.append((int(x[2][2:-1]), int(x[3][2:-1])))
    b.append((int(x[-2][2:-1]), int(x[-1][2:])))

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

global LO, HI
LO, HI = [0, 4 * 10**6]

d = [dist(s[i], b[i]) for i in range(n)]

def rep(ans):
    print(ans[0] * 4 * 10**6 + ans[1])
    return

def valid(pt):
    global LO, HI, n
    if pt[0] < LO or pt[1] < LO or pt[0] > HI or pt[1] > HI:
        return 0
    for i in range(n):
        if dist(pt, s[i]) <= d[i]:
            return 0
    return 1

for i in range(len(s)):
    print(i)
    sx, sy = s[i]
    bx, by = b[i]
    
    for sgn in [-1, 1]:
        x_lo = sx - d[i] - 1
        x_hi = sx + d[i] + 1
        y = sy
        while x_lo <= x_hi and LO <= y <= HI:
            if valid([x_lo, y]):
                rep([x_lo, y])
                TIME_()
                exit(0)
            if valid([x_hi, y]):
                rep([x_hi, y])
                TIME_()
                exit(0)
            x_lo += 1
            x_hi -= 1
            y += sgn

