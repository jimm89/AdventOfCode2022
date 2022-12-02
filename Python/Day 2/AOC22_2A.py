import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_2A_in.txt")

inp = [z.split() for z in f.read().split('\n')]

cols = [['A', 'B', 'C'], ['X', 'Y', 'Z']]

score = 0

for a, x in inp:
    score += cols[1].index(x) + 1
    i0, i1 = cols[0].index(a), cols[1].index(x)
    if i0 == i1:
        score += 3
        continue
    if i0 + 1 == i1 or i0 - 2 == i1:
        score += 6

print(score)