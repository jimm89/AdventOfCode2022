import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_21A_in.txt")

inp = [z.split() for z in f.read().split('\n')]

G = dd(list)

op = dd(str)

for x in inp:
    x[0] = x[0][:-1]
    if len(x) == 4:
        G[x[0]].append(x[1])
        G[x[0]].append(x[3])
        op[x[0]] = x[2] if x[2] != '/' else '//'
    else:
        G[x[0]].append(x[1])

def dfs(u):
    if len(G[u]) == 1:
        return G[u][0]
    return str(eval(dfs(G[u][0]) + op[u] + dfs(G[u][1])))

print(dfs('root'))