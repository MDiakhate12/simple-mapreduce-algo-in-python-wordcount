#!/usr/bin/env python

import sys


for line in sys.stdin:
    words = line.strip().split(" ")
    words = list(
        map(
            lambda word: word.lower() \
                .replace('.', '') \
                .replace(';', '') \
                .replace(':', '') \
                .replace(',', '') \
                .replace('"', '') \
            , words
            )
        )
    
    for word in words:
        if(word != "--"):
            print(f"{word} 1")

