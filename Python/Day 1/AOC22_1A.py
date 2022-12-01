import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_1A_in.txt")

inp = f.read().split('\n\n')
pairs = [sum(map(int,s.split('\n'))) for s in inp]

print(max(pairs))

