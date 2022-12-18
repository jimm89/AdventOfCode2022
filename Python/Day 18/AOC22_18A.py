import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_18A_in.txt")

inp = [list(map(int,x.split(','))) for x in f.read().split('\n')]

x, y, z = dd(set), dd(set), dd(set)

for a, b, c in inp:
    x[a].add((b,c))
    y[b].add((a,c))
    z[c].add((a,b))

n = len(inp)

ans = n * 6

m = 0

for a in x:
    for b, c in x[a]:
        if a + 1 in x and (b, c) in x[a + 1]:
            m += 2

for b in y:
    for a, c in y[b]:
        if b + 1 in y and (a, c) in y[b + 1]:
            m += 2

for c in z:
    for a, b in z[c]:
        if c + 1 in z and (a, b) in z[c + 1]:
            m += 2

print(ans - m)
                