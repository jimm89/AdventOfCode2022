import sys, copy, re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("AOC22_14A_in.txt")

inp = [x.split(' -> ') for x in f.read().split('\n')]

for i in range(len(inp)):
    for j in range(len(inp[i])):
        inp[i][j] = list(map(int, inp[i][j].split(',')))

# calculate min and 
def limit():
    max_ = 0
    for a in inp:
        for b in a:
            max_ = max(max_, b[1])
    return max_

y_max = limit()
grid = [['.']*1000 for x in range(y_max + 2)]

def draw_paths():
    for a in inp:
        for j in range(len(a) - 1):
            xs, ys = a[j]
            xe, ye = a[j + 1]
            # range loops want to move in positive direction
            if xs > xe:
                xs, xe = xe, xs
            if ys > ye:
                ys, ye = ye, ys
            for x in range(xs, xe + 1):
                for y in range(ys, ye + 1):
                    grid[y][x] = '#'

draw_paths()

ops = [0, -1, 1]

def run():
    ret = 0
    while True:
        x, y = [0, 500]
        while True:
            # if we've gone past y_max, then sand will fall forever
            if x == y_max + 1:
                return ret
            # try each possible move
            for j in range(3):
                if grid[x + 1][y + ops[j]] == '.':
                    x += 1
                    y += ops[j]
                    break
            else:
                break
        grid[x][y] = 'o'
        ret += 1

print(run())