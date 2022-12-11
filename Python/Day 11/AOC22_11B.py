import sys, copy, re, math
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_11A_in.txt")

inp = [s.split('\n') for s in f.read().split('\n\n')]

n = len(inp)

curr = [list(map(int, s[1][18:].split(', '))) for s in inp]
op = [s[2][23:] for s in inp]
test = [int(s[3][21:]) for s in inp]
true = list(map(int, [s[4].split()[-1] for s in inp]))
false = list(map(int, [s[5].split()[-1] for s in inp]))

cnt = [0]*n
LCM = 1

def lcm(a, b):
    return a * b // math.gcd(a, b)

for x in test:
    LCM = lcm(LCM, x)

for rnd in range(10000):
    for i in range(n):
        while curr[i]:
            old = curr[i][0]
            old = eval(str(old) + op[i])
            old %= LCM
            if old % test[i] == 0:
                curr[true[i]].append(old)
            else:
                curr[false[i]].append(old)
            curr[i].pop(0)
            cnt[i] += 1

cnt.sort()
print(cnt[-2] * cnt[-1])