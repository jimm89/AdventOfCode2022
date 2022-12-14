import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_13A_in.txt")

inp = [x.split('\n') for x in f.read().split('\n\n')]

ans = 0

def getfirst(arr):
    if arr.count(',') == 0:
        return -1
    ind = 1
    bal = 0
    while True:
        if ind == len(arr) - 1:
            assert(bal == 0)
            return -1
        if arr[ind] == ',' and bal == 0:
            return ind
        if arr[ind] == '[':
            bal += 1
        if arr[ind] == ']':
            bal -= 1
        ind += 1

def cmp(a, b):
    if a == '[]' and b == '[]':
        return 0
    if a == '[]':
        return 1
    if b == '[]':
        return -1
    if a[0] == '[' and b[0] == '[':
        i1 = getfirst(a)
        i2 = getfirst(b)
        x = a[1: i1]
        y = b[1: i2]
        z = cmp(x, y)
        if z == 1:
            return 1
        if z == -1:
            return -1
        if i1 == -1:
            a = '[]'
        else:
            a = '[' + a[i1 + 1: ]
        if i2 == -1:
            b = '[]'
        else:
            b = '[' + b[i2 + 1: ]
        return cmp(a, b)
    if a[0] != '[' and b[0] != '[':
        if int(a) < int(b):
            return 1
        if int(a) > int(b):
            return -1
        return 0
    if a[0] != '[':
        return cmp('[' + a + ']', b)
    return cmp(a, '[' + b + ']')
    

for i, p in enumerate(inp, start = 1):
    a, b = p
    if cmp(a, b) >= 0:
        ans += i

print(ans)