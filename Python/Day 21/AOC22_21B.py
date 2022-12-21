import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
from fraction import Fraction
f = open("AOC22_21A_in.txt")

inp = [z.split() for z in f.read().split('\n')]

G = dd(list)

op = dd(str)

for x in inp:
    x[0] = x[0][:-1]
    if len(x) == 4:
        G[x[0]].append(x[1])
        G[x[0]].append(x[3])
        op[x[0]] = x[2]# if x[2] != '/' else '//'
    else:
        G[x[0]].append(x[1])

def dfs(u):
    if len(G[u]) == 1:
        return G[u][0]
    if u == 'root':
        return dfs(G[u][0]), dfs(G[u][1])
    if op[u] == '/':
        return str(eval('Fraction(' + dfs(G[u][0]) + ',' + dfs(G[u][1]) + ')'))
    return str(eval(dfs(G[u][0]) + op[u] + dfs(G[u][1])))

L = 0
R = 10 ** 18

G['humn'] = ['0']
if dfs('root')[0] <= dfs('root')[1]:
    cmp = '<'
else:
    cmp = '>'

while R - L > 1:
    M = (L + R) >> 1
    G['humn'] = [str(M)]
    x, y = dfs('root')
    if eval(x) == eval(y):
        print(M)
        exit(0)
    if eval(str(eval(x)) + cmp + str(eval(y))):
        L = M
    else:
        R = M