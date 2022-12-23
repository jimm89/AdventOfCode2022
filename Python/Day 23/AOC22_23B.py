import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_23A_in.txt")

inp = [list(z) for z in f.read().split('\n')]

D = [[-1, 0], [1, 0], [0, -1], [0, 1]]
dirs = [[di, dj] for di in range(-1, 2) for dj in range(-1, 2) if di or dj]

n = len(inp)

for i in range(n):
    inp[i] = ['.'] * 2000 + inp[i] + ['.'] * 2000

m = len(inp[0])

for j in range(2000):
    inp = [['.'] * m] + inp
    inp.append(['.'] * m)

n = len(inp)

d = 0

elves = set()

for i in range(n):
    for j in range(m):
        if inp[i][j] == '#':
            elves.add((i, j))


rnd = 0
while True:
    rnd += 1
    cnt = dd(int)
    move = dd(tuple)
    for i, j in elves:
        # any neighbours
        if all([inp[i + di][j + dj] == '.' for di, dj in dirs]):
            continue
        for k in range(4):
            p = (d + k) % 4
            if p < 2: # try horizontally adjacent
                if not any([inp[i + D[p][0]][j + D[p][1] + dj] == '#' for dj in range(-1, 2)]):
                    move[(i, j)] = (i + D[p][0], j + D[p][1])
                    cnt[(i + D[p][0], j + D[p][1])] += 1
                    break
            else:
                if not any([inp[i + D[p][0] + di][j + D[p][1]] == '#' for di in range(-1, 2)]):
                    move[(i, j)] = (i + D[p][0], j + D[p][1])
                    cnt[(i + D[p][0], j + D[p][1])] += 1
                    break

    flag = True
    d = (d + 1) % 4
    for elf, mv in move.items():
        i, j = elf
        ii, jj = mv
        assert i != ii or j != jj
        if cnt[mv] == 1:
            flag = False
            inp[i][j] = '.'
            inp[ii][jj] = '#'
            elves.remove((i, j))
            elves.add((ii, jj))
    
    if flag:
        print(rnd)
        exit(0)
