import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_3A_in.txt")

inp = f.read().split('\n')

ans = 0

for x in inp:
    n = len(x)
    a, b = x[:n//2], x[n//2:]
    for i in range(26):
        c1, c2 = chr(ord('a') + i), chr(ord('A') + i)
        if c1 in a and c1 in b:
            ans += i + 1
        if c2 in a and c2 in b:
            ans += i + 27

print(ans)
