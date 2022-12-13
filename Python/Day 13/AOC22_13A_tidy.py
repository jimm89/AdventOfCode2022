import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_13A_in.txt")

inp = [x.split('\n') for x in f.read().split('\n\n')]

ans = 0

def cmp(a, b):
    t1 = type(a)
    t2 = type(b)
    if t1 == t2 == int:
        if a < b:
            return -1
        if a == b:
            return 0
        return 1
    if t1 == t2:
        if a == b:
            return 0
        if not a:
            return -1
        if not b:
            return 1
        z = cmp(a[0], b[0])
        if z:
            return z
        return cmp(a[1: ], b[1: ])
    if t1 == int:
        return cmp([a], b)
    return cmp(a, [b])
    

for i, p in enumerate(inp, start = 1):
    a, b = p
    a = eval(a)
    b = eval(b)
    if cmp(a, b) <= 0:
        ans += i

print(ans)