import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_2A_in.txt")

inp = [z.split() for z in f.read().split('\n')]

cols = [['A', 'B', 'C'], ['X', 'Y', 'Z']]

score = 0

for a, x in inp:
    score += cols[1].index(x) * 3
    i0, i1 = cols[0].index(a), cols[1].index(x)
    if (i1 == 0):
        i2 = (i0 - 1) % 3
    elif (i1 == 2):
        i2 = (i0 + 1) % 3
    else:
        i2 = i0
    score += i2 + 1

print(score)