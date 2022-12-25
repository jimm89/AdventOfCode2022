import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_25A_in.txt")

inp = f.read().split('\n')

ref = ['=', '-', '0', '1', '2']

def from_snafu(text):
    text = list(text)
    ans = 0
    mul = 1
    while text:
        x = text.pop()
        if '0' <= x <= '2':
            ans += int(x) * mul
        elif x == '-':
            ans -= mul
        else:
            ans -= 2 * mul
        mul *= 5
    return ans

def to_snafu(num):
    curr = 1
    tot = 2
    LEN = 0
    while num > tot:
        curr *= 5
        tot += 2 * curr
        LEN += 1
    if tot - num < curr:
        ret = "2"
        num -= curr
    else:
        ret = "1"
    tot //= 5
    num -= tot + 1
    rst = ""
    assert num >= 0
    while num:
        rst += ref[num % 5]
        num //= 5
    while len(rst) < LEN:
        rst += '='
    return ret + rst[::-1]

ans = 0

for x in inp:
    ans += from_snafu(x)

print(to_snafu(ans))