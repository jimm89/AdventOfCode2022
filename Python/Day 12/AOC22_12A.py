import sys, copy, re, heapq as h
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_12A_in.txt")

inp = [list(s) for s in f.read().split('\n')]

n = len(inp)
m = len(inp[0])

grid = [[ord(inp[i][j]) - ord('a') for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == -14:
            curr = [i, j]
            grid[i][j] = 0
        if grid[i][j] == -28:
            end = [i, j]
            grid[i][j] = 25

G = dd(list)

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        for k in range(4):
            if 0 <= i + di[k] < n and 0 <= j + dj[k] < m and grid[i + di[k]][j + dj[k]] <= grid[i][j] + 1:
                G[(i, j)].append((i + di[k], j + dj[k]))

q = [(0, curr)]

dist = [[100000 for j in range(m)] for i in range(n)]
dist[curr[0]][curr[1]] = 0


while q:
    d, pos = h.heappop(q)
    i, j = pos
    for x, y in G[(i, j)]:
        if dist[x][y] > d + 1:
            h.heappush(q, (d + 1, [x, y]))
            dist[x][y] = d + 1

print(dist[end[0]][end[1]])