#!/usr/bin/env python3
import argparse


with open('data.txt') as f:
    data = f.readlines()


def _run_1():
    global data
    presents = []
    for d in data:
        presents.append({'dimensions': map(int, d.strip('\n').split('x'))})
    
    for i, p in enumerate(presents):
        a, l, w = p['dimensions']
        sides = [a*l, a*w, l*w]
        min_side = min(sides)
        presents[i]['paper'] = sum(2*s for s in sides) + min_side

    print(sum(p['paper'] for p in presents))


def _run_2():
    global data
    presents = []
    for d in data:
        presents.append({'dimensions': [int(c) for c in d.strip('\n').split('x')]})
    
    for i, p in enumerate(presents):
        a, l, w = p['dimensions']
        volume = a*l*w
        min_sides = sorted(p['dimensions'])[:2]
        presents[i]['ribbon'] = 2*sum(min_sides) + volume

    print(sum(p['ribbon'] for p in presents))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', default=1)
    args = parser.parse_args()
    if args.part == 1:
        _run_1()
    else:
        _run_2()
