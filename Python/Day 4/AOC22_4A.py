import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_4A_in.txt")

inp = [x.split(',') for x in f.read().split('\n')]

ans = 0

for a, b in inp:
    a = list(map(int,a.split('-')))
    b = list(map(int,b.split('-')))
    if b[0] >= a[0] and b[1] <= a[1]:
        ans += 1
    elif b[0] <= a[0] and b[1] >= a[1]:
        ans += 1

print(ans)
    
    