#!/usr/bin/env python3
import argparse


def _run_1(data):
    pass


def _run_2(data):
    pass


if __name__ == '__main__':
    with open('data.txt') as f:
        data = f.readlines()

    parser = argparse.ArgumentParser()
    parser.add_argument('--part', '-p', default=1)
    args = parser.parse_args()
    if args.part == 1:
        _run_1(data)
    else:
        _run_2(data)
