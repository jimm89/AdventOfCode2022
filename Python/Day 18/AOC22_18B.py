import sys, copy, re
from collections import defaultdict as dd, deque as dq
read = sys.stdin.read
f = open("AOC22_18A_in.txt")

inp = [list(map(int,x.split(','))) for x in f.read().split('\n')]

x, y, z = dd(set), dd(set), dd(set)
pts = set()

for a, b, c in inp:
    x[a].add((b,c))
    y[b].add((a,c))
    z[c].add((a,b))
    pts.add((a, b, c))


n = len(inp)

G = dd(list)

m = 0

for a in x:
    for b, c in x[a]:
        if a + 1 in x and (b, c) in x[a + 1]:
            m += 2

for b in y:
    for a, c in y[b]:
        if b + 1 in y and (a, c) in y[b + 1]:
            m += 2

for c in z:
    for a, b in z[c]:
        if c + 1 in z and (a, b) in z[c + 1]:
            m += 2


ops = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

"""
    consider the inside of each cube a node, and also the face of each cube a node
    there is an edge between the inside and the face unless there's a cube there
"""

for i in range(20):
    for j in range(20):
        for k in range(20):
            if (i, j, k) in pts:
                continue
            for a, b, c in ops:
                G[(i, j, k, 0, 0, 0)].append((i, j, k, a, b, c))
                G[(i, j, k, a, b, c)].append((i, j, k, 0, 0, 0))

for i in range(-1, 21):
    for j in range(-1, 21):
        for k in range(-1, 21):
            for a, b, c in ops:
                G[(i, j, k, a, b, c)].append((i + a, j + b, k + c, -a, -b, -c))
            

source = (-10, -10, -10, -10, -10, -10)

for i in range(20):
    for j in range(20):
        for a, b, c in ops:
            G[source].append((i, j, 19, 0, 0, 1))
            G[source].append((i, j, 0, 0, 0, -1))
            G[source].append((i, 19, j, 0, 1,0))
            G[source].append((i, 0, j, 0, -1,0))
            G[source].append((19, i, j, 1, 0,0))
            G[source].append((0, i, j, -1, 0,0))

# bfs from source
vis = set()
q = dq([source])

while q:
    cell = q.popleft()
    vis.add(cell)
    for neigh in G[cell]:
        if neigh not in vis:
            vis.add(neigh)
            q.append(neigh)

ans = 0

for i, j, k in pts:
    for a, b, c in ops:
        if (i, j, k, a, b, c) in vis:
            ans += 1

print(ans)