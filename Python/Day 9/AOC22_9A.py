import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read

f = open("AOC22_9A_in.txt")
inp = [s.split() for s in f.read().split('\n')]

vis = set()

vis.add((0, 0))

h = [0, 0]
t = [0, 0]

def touch(h, t):
    return abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1

def move(h, a):
    if a == "R":
        h[1] += 1
    elif a == "L":
        h[1] -= 1
    elif a == "D":
        h[0] -= 1
    else:
        h[0] += 1
    return h
    

for a, b in inp:
    b = int(b)
    for _ in range(b):
        h = move(h, a)
        if not touch(h, t):
            if h[0] == t[0] + 2:
                t[0] += 1
                t[1] = h[1]
            elif h[0] == t[0] - 2:
                t[0] -= 1
                t[1] = h[1]
            elif h[1] == t[1] + 2:
                t[1] += 1
                t[0] = h[0]
            else:
                t[1] -= 1
                t[0] = h[0]
        assert touch(h, t)
        vis.add(tuple(t))

print(len(set(vis)))