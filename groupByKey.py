#!/usr/bin/env python

import sys

count = 0
previousKey = None

for line in sys.stdin:
    currentKey, currentValue = line.strip().split()
    if(currentKey == previousKey):
        count += f"{currentValue} "
    else:
        if(previousKey != None):
            print(previousKey, count)

        count = f"{currentValue} "
    
    previousKey = currentKey

print(previousKey, count)
