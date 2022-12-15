"""

    This solution runs in negligible time on Python

"""

import sys, copy, re
import time

start_time = time.time()
def TIME_(): print(time.time()-start_time)

from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_15A_in.txt")

inp = [line.split() for line in f.read().split('\n')]

n = len(inp)
s, b = [], []

for x in inp:
    s.append((int(x[2][2:-1]), int(x[3][2:-1])))
    b.append((int(x[-2][2:-1]), int(x[-1][2:])))

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

d = [dist(s[i], b[i]) for i in range(n)]

vecs = dd(list)

"""
    find intersection of four different lines at distances d + 1 from their respective points
    line has gradient dy/dx, direction [dx, dy]
    line is at distance d + 1 from the point sx, sy
    
    if dx = 1, then the point (sx - d - 1, sy) is on the line
    otherwise the point (sx + d + 1, sy) is on the line
    
    so generally speaking the point (sx - (d + 1) * dx, sy) is on the line
    y = dy/dx * (x - sx + dx * (d + 1)) + sy
    
    m = dy/dx, c = sy + dy * (d + 1) - dy/dx * sx
"""    

vec_direction = [set() for _ in range(4)]

for i in range(n):
    idx = -1
    for dx in [-1, 1]:
        for dy in [-1, 1]:
            idx += 1
            m = dy * dx # same as dy // dx
            c = s[i][1] + dy * (d[i] + 1) - m * s[i][0]
            vec_direction[idx].add((m, c))

"""

    Now let's find the common intercepts is sets 0 and 3, sets 1 and 2.
    They each should have set size 1, and then we find the intersection of those two lines
    
    y = m1 * x + c1
    y = m2 * x + c2
    (m1 - m2) * x = c2 - c1

"""

common_intercepts = [vec_direction[0].intersection(vec_direction[3])]
common_intercepts.append(vec_direction[1].intersection(vec_direction[2]))

assert len(common_intercepts[0]) == len(common_intercepts[1]) == 1

m1, c1 = next(iter(common_intercepts[0]))
m2, c2 = next(iter(common_intercepts[1]))

x = (c2 - c1) // (m1 - m2)
y = m1 * x + c1

print(x * 4000000 + y)
TIME_()