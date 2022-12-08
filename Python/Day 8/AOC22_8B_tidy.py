import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read

f = open("AOC22_8A_in.txt")
inp = [list(map(int, list(x))) for x in f.read().split('\n')]

n = len(inp)
m = len(inp[0])

ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
lim = [-1, n, -1, m]

for i in range(n):
    for j in range(m):
        v = inp[i][j]
        score = 1
        for k in range(4):
            curr = 0
            i0, j0 = i, j
            while i0 + dx[k] != lim[k] and j0 + dy[k] != lim[k]:
                i0 += dx[k]
                j0 += dy[k]
                curr += 1
                if inp[i0][j0] >= v:
                    break
            score *= curr
        ans = max(ans, score)
        
        
print(ans)