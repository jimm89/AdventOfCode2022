import sys, copy, re
from collections import defaultdict as dd, deque as dq
read = sys.stdin.read
f = open("AOC22_18A_in.txt")

inp = [list(map(int,x.split(','))) for x in f.read().split('\n')]

pts = set()

for a, b, c in inp:
    pts.add((a, b, c))

G = dd(list)

faces = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

"""
    consider the inside of each cube a node, and also the face of each cube a node
    there is an edge between the inside and the face unless there's a cube there
"""
mn = 0
mx = 19

for i in range(mn, mx + 1):
    for j in range(mn, mx + 1):
        for k in range(mn, mx + 1):
            if (i, j, k) in pts:
                continue
            for a, b, c in faces:
                G[(i, j, k, 0, 0, 0)].append((i, j, k, a, b, c))
                G[(i, j, k, a, b, c)].append((i, j, k, 0, 0, 0))

# must also have an edge from one side of the face to the other
for i in range(mn, mx + 1):
    for j in range(mn, mx + 1):
        for k in range(mn, mx + 1):
            for a, b, c in faces:
                G[(i, j, k, a, b, c)].append((i + a, j + b, k + c, -a, -b, -c))
            

source = (-1, ) # different length guarantees uniqueness

# an external 'source' node flows to the outer most faces only
for i in range(mn, mx + 1):
    for j in range(mn, mx + 1):
        for q in faces:
            sm = sum(q)
            idx = q.index(sm)
            rotate = (idx + 1) % 3
            pt = [i, j, mx if sm > 0 else mn]
            pt = tuple(pt[-rotate : ] + pt[ : -rotate])
            G[source].append(pt + q)

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

# count the number of faces of cubes in the set which can be reached from the source, i.e. are in vis
for i, j, k in pts:
    for a, b, c in faces:
        if (i, j, k, a, b, c) in vis:
            ans += 1

print(ans)