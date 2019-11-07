#!/usr/bin/env python3
import argparse
from collections import namedtuple


Instruction = namedtuple('Instruction', ['op', 'args', 'wire'])


def _try_coerce_to_int(token):
    try:
        return int(token)
    except ValueError:
        return token


def _parse_instruction(d):
    tokens = d.split()
    op = None
    args = None
    wire = tokens[-1]

    if len(tokens) == 3:
        op = 'store'
        args = (_try_coerce_to_int(tokens[0]),)
    elif len(tokens) == 4:
        op = 'not'
        args = (_try_coerce_to_int(tokens[1]),)
    elif len(tokens) == 5:
        op = tokens[1].lower()
        args = tuple(map(_try_coerce_to_int, [tokens[0], tokens[2]]))

    return Instruction(op, args, wire)



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
