#!/usr/bin/env python3
frequency_changes = []


with open('data.txt') as f:
    for l in f.readlines():
        frequency_changes.append(int(l))


print(sum(frequency_changes))
