import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read

inp = ['BQC', 'RQWZ', 'BMRLV', 'CZHVTW', 'DZHBNVG', 'HNPCJFVQ', 'DGTRWZS', 'CGMNBWZP', 'NJBMWQFP']

inp = [list(s) for s in inp]

f = open("AOC22_5A_in.txt")
ins = [z.split() for z in f.read().split('\n')]

for a, b, c, d, e, f in ins:
    b = int(b)
    d = int(d) - 1
    f = int(f) - 1
    for j in range(b):
        inp[f].append(inp[d][j - b])
    inp[d] = inp[d][:-b]
    
ans = [x[-1] for x in inp]

print(''.join(ans))

