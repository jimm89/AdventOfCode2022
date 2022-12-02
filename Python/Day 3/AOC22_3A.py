import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_3A_in.txt")

inp = [z.split() for z in f.read().split('\n')]

cols = [['A', 'B', 'C'], ['X', 'Y', 'Z']]

score = 0

for a, x in inp:
    i0, i1 = cols[0].index(a), cols[1].index(x)
    score += i1 * 3
    i2 = (i0 - 1 + i1) % 3
    score += i2 + 1

print(score)