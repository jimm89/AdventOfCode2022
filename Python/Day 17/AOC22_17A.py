import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_17A_in.txt")

inp = f.read()

g = open("rocks.txt")
rocks = [list(reversed(list(z.split('\n')))) for z in g.read().split('\n\n')]
#print(rocks)

grid = [['.']*7 for _ in range(20000)]

num = 2022
h = -1
curr = 0


for k in range(num):
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

print(h + 1)
#grid.reverse()
