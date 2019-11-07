#!/usr/bin/env python3
import argparse


with open('data.txt') as f:
    data = f.readline()


def _run_1():
    global data
    floor = 0
    for c in data:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
    print(floor)


def _run_2():
    global data
    floor = 0
    for p, c in enumerate(data):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor == -1:
            print(p+1)
            return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', default=1)
    args = parser.parse_args()
    if args.part == 1:
        _run_1()
    else:
        _run_2()
