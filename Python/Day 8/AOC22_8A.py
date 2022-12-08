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
        flag = False
        v = inp[i][j]
        tmp = True
        for k in range(i):
            tmp &= inp[k][j] < v
        flag |= tmp
        tmp = True
        for k in range(i + 1, n):
            tmp &= inp[k][j] < v
        flag |= tmp
        tmp = True
        for k in range(j):
            tmp &= inp[i][k] < v
        flag |= tmp
        tmp = True
        for k in range(j + 1, m):
            tmp &= inp[i][k] < v
        flag |= tmp
        if flag:
            ans += 1

print(ans)

