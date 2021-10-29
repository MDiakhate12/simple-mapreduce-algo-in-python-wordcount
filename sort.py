#!/usr/bin/env python

import sys

lines = []

for (index, line) in enumerate(sys.stdin):
    key, value = line.split()
    lines.append((key, value))

lines.sort()

for line in lines:
    print(f"{line[0]} {line[1]}")