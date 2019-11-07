#!/usr/bin/env python3
import argparse
from collections import defaultdict


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, order):
        if order == '^':
            self.y += 1
        elif order == 'v':
            self.y -= 1
        elif order == '>':
            self.x += 1
        elif order == '<':
            self.x -= 1

    def as_tuple(self):
        return (self.x, self.y)


with open('data.txt') as f:
    data = f.readline()


def _run_1():
    global data
    p_map = defaultdict(int)
    p = Position(0, 0)
    p_map[p.as_tuple()] += 1

    for order in data.strip('\n'):
        p.move(order)
        p_map[p.as_tuple()] += 1

    print(len(p_map))


def _run_2():
    global data
    p_map = defaultdict(int)
    s = Position(0, 0)
    r = Position(0, 0)
    p_map[s.as_tuple()] += 1
    p_map[r.as_tuple()] += 1

    for i, order in enumerate(data.strip('\n')):
        if i % 2:
            s.move(order)
            coord = s.as_tuple()
        else:
            r.move(order)
            coord = r.as_tuple()
        p_map[coord] += 1

    print(len(p_map))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', default=1)
    args = parser.parse_args()
    if args.part == 1:
        _run_1()
    else:
        _run_2()
