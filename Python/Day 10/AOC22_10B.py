import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_10A_in.txt")

inp = f.read().split('\n')

cyc = 1
curr = 1
ans = 0

rows = [['.'] * 40 for _ in range(6)]

for i, x in enumerate(inp):
    x = x.split()
    if (curr + 1 - cyc) % 40 <= 1 or (cyc - 1 - curr) % 40 <= 1:
        rows[(cyc - 1) // 40][(cyc - 1) % 40] = '#'
    cyc += 1
    if len(x) == 1:
        continue
    if (curr + 1 - cyc) % 40 <= 1 or (cyc - 1 - curr) % 40 <= 1:
        rows[(cyc - 1) // 40][(cyc - 1) % 40] = '#'
    curr += int(x[1])
    cyc += 1

for row in rows:
    print(*row, sep = '')