import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_10A_in.txt")

inp = f.read().split('\n')

cyc = 1
curr = 1
ans = 0

for x in inp:
    x = x.split()
    if cyc % 40 == 20:
        ans += cyc * curr
    cyc += 1
    if len(x) == 1:
        continue
    if cyc % 40 == 20:
        ans += cyc * curr
    curr += int(x[1])
    cyc += 1
print(ans)