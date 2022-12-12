import sys, copy, re, heapq as h
from collections import defaultdict as dd, deque as dq
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

big = 100000
dist = [[big for j in range(m)] for i in range(n)]

# multi-source BFS using deque

q = dq([])

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            dist[i][j] = 0
            q.append((0, [i, j])) # add all start points to the BFS queue with distance zero
            

while q:
    d, pos = q.popleft()
    i, j = pos
    for x, y in G[(i, j)]:
        if dist[x][y] == big:
            dist[x][y] = d + 1
            q.append((d + 1, [x, y]))

print(dist[end[0]][end[1]])