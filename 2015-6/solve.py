#!/usr/bin/env python3
import argparse
from collections import namedtuple

from tqdm import tqdm


Instruction = namedtuple('Instruction', ['action', 'from_x', 'from_y', 'to_x', 'to_y'])


def _execute(grid, i):
    for m in range(i.from_x, i.to_x + 1):
        for n in range(i.from_y, i.to_y + 1):
            if i.action == 'on':
                grid[m][n] = 1
            elif i.action == 'off':
                grid[m][n] = -1
            elif i.action == 'toggle':
                grid[m][n] *= -1


def _regulate(grid, i):
    for m in range(i.from_x, i.to_x + 1):
        for n in range(i.from_y, i.to_y + 1):
            if i.action == 'on':
                grid[m][n] += 1
            elif i.action == 'off':
                grid[m][n] -= 1
                if grid[m][n] < 0:
                    grid[m][n] = 0
            elif i.action == 'toggle':
                grid[m][n] += 2


def _parse_instructions(data):
    instructions = []

    for d in data:
        tokens = d.split()
        coord_tokens = tokens[2:]
        params = {}

        if tokens[0] == 'toggle':
            params['action'] = 'toggle'
            coord_tokens = tokens[1:]
        elif tokens[1] == 'on':
            params['action'] = 'on'
        elif tokens[1] == 'off':
            params['action'] = 'off'

        params['from_x'], params['from_y'] = map(int, coord_tokens[0].split(','))
        params['to_x'], params['to_y'] = map(int, coord_tokens[2].split(','))

        instructions.append(Instruction(**params))

    return instructions


def _run_1(data):
    grid = [[-1 for _ in range(1000)] for _ in range(1000)]

    instructions = _parse_instructions(data)

    for i in tqdm(instructions):
        _execute(grid, i)

    flat_grid = [l for row in grid for l in row]
    print(len([l for l in flat_grid if l > 0]))


def _run_2(data):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    instructions = _parse_instructions(data)

    for i in tqdm(instructions):
        _regulate(grid, i)

    flat_grid = [b for row in grid for b in row]
    print(sum(flat_grid))


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
