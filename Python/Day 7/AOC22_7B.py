import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read

f = open("AOC22_7A_in.txt")
inp = f.read().split('\n')

ans = 0

path = []
sz = dd(int)

"""

if cd, then we go into a folder or come out
if we go in, then everything inside

/ -> (a, b, c)

add b and c to the path

If we go into folder, add that folder to the path, ls
If ls, ignore anything that's a dir, add anything that isn't to everything on the current path
If we come out of folder, remove top node from path

"""

for line in inp:
    x = line.split()
    if x[0] == "$" and x[1] == "cd":
        if x[2] == "..":
            path.pop()
        else:
            path.append(x[2])
        continue
    if x[0] == "$":
        assert x[1] == "ls"
        continue
    if x[0] == "dir":
        continue
    for i in range(len(path)):
        sz[''.join(path[:i + 1])] += int(x[0])

allowed = 70000000
req = 30000000
used = sz["/"]
unused = allowed - used
rem = req - unused

ans = 10**10

for key, val in sz.items():
    if val >= rem:
        ans = min(ans, val)

print(ans)