#!/usr/bin/env python3
import argparse
import hashlib


with open('data.txt') as f:
    data = f.readline()


def _run_1():
    global data
    key = data.strip('\n')
    n = 0
    hash_ = hashlib.md5(f'{key}{n}'.encode()).hexdigest()

    while not hash_.startswith('000000'):
        n += 1
        hash_ = hashlib.md5(f'{key}{n}'.encode()).hexdigest()

    print(n)



def _run_2():
    global data
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', default=1)
    args = parser.parse_args()
    if args.part == 1:
        _run_1()
    else:
        _run_2()
