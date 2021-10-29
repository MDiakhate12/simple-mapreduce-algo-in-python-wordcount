#!/usr/bin/env python

import sys 

for line in sys.stdin:
    count = 0
    key, values = line.split(" ", 1)
    for value in values.split():
        count += int(value)
    print(f"{key} {count}")