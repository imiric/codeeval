#!/usr/bin/env python2
# Yodle - Pass Triangle
# https://www.codeeval.com/open_challenges/89/
# Author: Ivan Miric <imiric@gmail.com>

import sys


f = open(sys.argv[1], 'r')
triangle = f.readlines()
f.close()

paths = []

for row in triangle:
    nodes = [int(r) for r in row.strip().split(' ')]
    if len(nodes) == 1:
        paths.append([nodes[0]])
        continue
    p = paths[:]
    for i in range(len(p)):
        #if nodes == [0, 7, 1, 5]:
            #import ipdb; ipdb.set_trace()
        curr = p[i]
        c = curr[:]
        c.append(nodes[i])
        paths[i] = c
        if len(nodes)-1 > i:
            c = curr[:]
            c.append(nodes[i+1])
            paths.append(c)
        else:
            c = curr[:]
            c.append(nodes[i-1])
            paths.append(c)

print paths

max_total = 0
for p in paths:
    total = sum(p)
    if total > max_total:
        max_total = total

print max_total
