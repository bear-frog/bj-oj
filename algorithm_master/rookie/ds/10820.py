#!/usr/bin/python3
import sys
lines = sys.stdin.readlines()
for s in lines:
    low = 0
    up = 0
    num = 0
    space = 0
    sl = list(s)
    for e in sl:
        if e.isupper():
            up += 1
        if e.islower():
            low += 1
        if e.isdigit():
            num += 1
        if e == ' ':
            space += 1
    print(low, up, num, space)
