import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_2A_in.txt")

inp = [z.split() for z in f.read().split('\n')]

cols = [['A', 'B', 'C'], ['X', 'Y', 'Z']]

score = 0

for a, x in inp:
    i0, i1 = cols[0].index(a), cols[1].index(x)
    score += i1 + 1
    diff = i1 - i0
    score += ((diff + 1) % 3) * 3

print(score)