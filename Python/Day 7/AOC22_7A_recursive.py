import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read

f = open("AOC22_7A_in.txt")
inp = f.read().split('\n')

ans = 0

G = dd(list)
sz = dd(int)
path = []

for line in inp:
    x = line.split()
    if x[0] == "$" and x[1] == "cd":
        if x[2] == "..":
            path.pop()
        elif not path:
            path.append(".")
        else:
            path.append(path[-1] + "/" + x[2])
        continue
    if x[0] == "$":
        assert x[1] == "ls"
        continue
    if '0' <= x[0][0] <= '9':
        sz[path[-1]] += int(x[0])
    else:
        G[path[-1]].append(path[-1] + "/" + x[1])

#print(G)

def dfs(u):
    for v in G[u]:
        dfs(v)
        sz[u] += sz[v]

dfs(".")

for key, val in sz.items():
    if val <= 100000:
        ans += val

print(ans)
