import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_17A_in.txt")

inp = f.read()

g = open("rocks.txt")
rocks = [list(reversed(list(z.split('\n')))) for z in g.read().split('\n\n')]

grid = [['.']*7 for _ in range(100)]

num = 1000000000000
h = -1
curr = 0

vis = {}
period = {}
added = 0
k = 0

while k < num:
    rock = rocks[k % 5]
    x = h + 4
    y = 2
    n = len(rock)
    m = len(rock[0])
    sq = []
    for i in range(n):
        for j in range(m):
            if rock[i][j] == '#':
                sq.append([x + i, y + j])
    while True:
        if inp[curr] == '>':
            if all([z[1] < 6 and grid[z[0]][z[1] + 1] == '.' for z in sq]):
                for i in range(len(sq)):
                    sq[i][1] += 1
        else:
            if all([z[1] > 0 and grid[z[0]][z[1] - 1] == '.' for z in sq]):
                for i in range(len(sq)):
                    sq[i][1] -= 1
        curr = (curr + 1) % len(inp)
        if all([z[0] > 0 and grid[z[0] - 1][z[1]] == '.' for z in sq]):
            for i in range(len(sq)):
                sq[i][0] -= 1
        else:
            break
    for x, y in sq:
        grid[x][y] = '#'
        h = max(h, x)
    shift = 40 # answer appears to stabilise at shift >= 36
    if h > shift:
        added += h - shift
        grid = grid[h - shift : h + 1]
        grid += [['.'] * 7 for j in range(50 - len(grid))]
        h = shift
    tg = tuple(tuple(g) for g in grid)
    check = (tg, curr, k % 5)
    if check in vis:
        prev_k, prev_h = vis[check]
        diff_h = h + added - prev_h
        diff_k = k - prev_k
        if check not in period:
            period[check] = diff_k
        reps = (num - k) // period[check]
        added += reps * diff_h
        k += reps * diff_k
    vis[check] = (k, h + added)
    k += 1

print(h + added + 1)