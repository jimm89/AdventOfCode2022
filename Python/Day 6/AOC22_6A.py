import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read

f = open("AOC22_6A_in.txt")
inp = f.read()

for i in range(3, len(inp)):
    if (len(set(inp[i - 3: i + 1])) == 4):
        print(i + 1)
        break



