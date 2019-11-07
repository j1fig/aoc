#!/usr/bin/env python3
import argparse
import re


with open('data.txt') as f:
    data = f.readlines()


def _count_vowels(sentence):
    vowel_count = 0
    vowels = ('a', 'e', 'i', 'o', 'u')
    for v in vowels:
        matches = [m.start() for m in re.finditer(v, sentence)]
        vowel_count += len(matches)

    return vowel_count


def _has_repeated_consecutive_characters(sentence):
    last = sentence[0]

    for c in sentence[1:]:
        if c == last:
            return True
        last = c

    return False


def _has_evil_sequence(sentence):
    evil = ('ab', 'cd', 'pq', 'xy')
    return any(e in sentence for e in evil)


def _run_1():
    global data
    nice = 0

    for s in data:
        vowels = _count_vowels(s)
        if vowels < 3:
            continue

        if not _has_repeated_consecutive_characters(s):
            continue

        if _has_evil_sequence(s):
            continue

        nice += 1

    print(nice)


def _has_non_overlapping_repeating_pairs(sentence):
    pair = sentence[0:2]

    for i, _ in enumerate(sentence[2:]):
        if pair in sentence[i+2:]:
            return True
        pair = sentence[i+1:i+3]

    return False


def _has_interspersed_repeated_letters(sentence):
    last = sentence[0]

    for i, c in enumerate(sentence[2:]):
        if c == last:
            return True
        last = sentence[1+i]

    return False


def _run_2():
    global data
    nice = 0

    for s in data:
        if not _has_non_overlapping_repeating_pairs(s):
            continue
        if not _has_interspersed_repeated_letters(s):
            continue

        nice += 1

    print(nice)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', default=1)
    args = parser.parse_args()
    if args.part == 1:
        _run_1()
    else:
        _run_2()
