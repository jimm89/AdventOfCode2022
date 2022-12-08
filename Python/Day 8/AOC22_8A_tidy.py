import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read

f = open("AOC22_8A_in.txt")
inp = [list(map(int, list(x))) for x in f.read().split('\n')]

n = len(inp)
m = len(inp[0])

ans = 0

for i in range(n):
    for j in range(m):
        v = inp[i][j]
        
        b1 = all([inp[k][j] < v for k in range(i)])
        b2 = all([inp[k][j] < v for k in range(i + 1, n)])
        b3 = all([inp[i][k] < v for k in range(j)])
        b4 = all([inp[i][k] < v for k in range(j + 1, m)])
        
        ans += any([b1, b2, b3, b4])
        
print(ans)

