import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_23A_in.txt")

inp = [list(z) for z in f.read().split('\n')]

D = [[-1, 0], [1, 0], [0, -1], [0, 1]]
dirs = [[di, dj] for di in range(-1, 2) for dj in range(-1, 2) if di or dj]

n = len(inp)

for i in range(n):
    inp[i] = ['.'] * 12 + inp[i] + ['.'] * 12

m = len(inp[0])

for j in range(12):
    inp = [['.'] * m] + inp
    inp.append(['.'] * m)

n = len(inp)

d = 0


for _ in range(10):
    cnt = dd(int)
    move = dd(tuple)
    for i in range(n):
        for j in range(m):
            if inp[i][j] == '.':
                continue
            # any neighbours
            if all([inp[i + di][j + dj] == '.' for di, dj in dirs]):
                continue
            for k in range(4):
                p = (d + k) % 4
                ds = [[x * (abs(D[p][0]) ^ 1), x * (abs(D[p][1]) ^ 1)] for x in range(-1, 2)]
                if not any([inp[i + D[p][0] + di][j + D[p][1] + dj] == '#' for di, dj in ds]):
                    move[(i, j)] = (i + D[p][0], j + D[p][1])
                    cnt[(i + D[p][0], j + D[p][1])] += 1
                    break
                
    d = (d + 1) % 4
    for elf, mv in move.items():
        i, j = elf
        ii, jj = mv
        assert i != ii or j != jj
        if cnt[mv] == 1:
            inp[i][j] = '.'
            inp[ii][jj] = '#'

mn = [100000] * 2
mx = [-1] * 2

num = 0

for i in range(n):
    for j in range(m):
        if inp[i][j] == '#':
            num += 1
            mn[0] = min(mn[0], i)
            mx[0] = max(mx[0], i)
            mn[1] = min(mn[1], j)
            mx[1] = max(mx[1], j)



print((mx[0] - mn[0] + 1) * (mx[1] - mn[1] + 1) - num)