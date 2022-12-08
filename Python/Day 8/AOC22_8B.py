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
        score = 1

        k = i
        while k - 1 >= 0 and inp[k - 1][j] < v:
            k -= 1
        if k > 0:
            k -= 1
        score *= (i - k)
        
        k = i
        while k + 1 < n and inp[k + 1][j] < v:
            k += 1
        if k < n - 1:
            k += 1
        score *= (k - i)
        
        k = j
        while k - 1 >= 0 and inp[i][k - 1] < v:
            k -= 1
        if k > 0:
            k -= 1
        score *= (j - k)
        
        k = j
        while k + 1 < m and inp[i][k + 1] < v:
            k += 1
        if k < m - 1:
            k += 1
        score *= (k - j)
        
        ans = max(ans, score)

print(ans)

