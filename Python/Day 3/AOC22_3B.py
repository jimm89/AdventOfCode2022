import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_3A_in.txt")

inp = f.read().split('\n')

ans = 0

for i in range(len(inp) // 3):
    x, y, z = inp[i * 3], inp[i * 3 + 1], inp[i * 3 + 2]
    for j in range(26):
        c1, c2 = chr(ord('a') + j), chr(ord('A') + j)
        if c1 in x and c1 in y and c1 in z:
            ans += j + 1
        if c2 in x and c2 in y and c2 in z:
            ans += j + 27

print(ans)
