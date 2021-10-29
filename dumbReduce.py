#!/usr/bin/env python

import sys 

count = 0
previousKey = None

for line in sys.stdin:
    currentKey, currentValue = line.strip().split()
    if(currentKey == previousKey):
        count += f"{currentValue} "
    else:
        print(f"{previousKey} {count}")
        count = f"{currentValue} "
    
    previousKey = currentKey

for line in sys.stdin:
    count = 0
    key, values = line.split(" ", 1)
    for value in values.split():
        count += int(value)
    print(f"{key} {count}")