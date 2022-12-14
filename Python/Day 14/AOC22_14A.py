import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_14A_in.txt")

inp = [x.split(' -> ') for x in f.read().split('\n')]

for i in range(len(inp)):
    for j in range(len(inp[i])):
        inp[i][j] = list(map(int, inp[i][j].split(',')))

x_min = 500
x_max = 500
y_min = 0
y_max = 0

for a in inp:
    for b in a:
        x_min = min(x_min, b[0])
        x_max = max(x_max, b[0])
        y_min = min(y_min, b[1])
        y_max = max(y_max, b[1])

grid = [['.']*1000 for x in range(y_max + 15)]

# print the grid for debugging
def pg():
    for g in grid[:40]:
        print(*g[x_min + 30: x_max + 5], sep = '')

for a in inp:
    for j in range(len(a) - 1):
        xs, ys = a[j]
        xe, ye = a[j + 1]
        if xs > xe:
            xs, xe = xe, xs
        if ys > ye:
            ys, ye = ye, ys
        for x in range(xs, xe + 1):
            for y in range(ys, ye + 1):
                grid[y][x] = '#'

ans = 0

while True:
    pos = [0, 500]
    while True:
        if pos[0] > y_max + 5:
            print(ans)
            exit(0)
        if grid[pos[0] + 1][pos[1]] == '.':
            pos[0] += 1
        elif grid[pos[0] + 1][pos[1] - 1] == '.':
            pos[0] += 1
            pos[1] -= 1
        elif grid[pos[0] + 1][pos[1] + 1] == '.':
            pos[0] += 1
            pos[1] += 1
        else:
            break
    grid[pos[0]][pos[1]] = 'o'
    ans += 1

pg()