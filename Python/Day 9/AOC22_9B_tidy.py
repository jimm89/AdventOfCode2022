import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read

f = open("AOC22_9A_in.txt")
inp = [s.split() for s in f.read().split('\n')]

vis = set()

vis.add((0, 0))

H = [[0, 0] for _ in range(10)]

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
        H[0] = move(H[0], a)
        for i in range(9):
            if not touch(H[i], H[i + 1]):
                for j in range(2):
                    diff = H[i][j] - H[i + 1][j]
                    if abs(diff) > 1:
                        diff //= abs(diff)
                    H[i + 1][j] += diff
            assert touch(H[i], H[i + 1])
        vis.add(tuple(H[9]))

print(len(set(vis)))