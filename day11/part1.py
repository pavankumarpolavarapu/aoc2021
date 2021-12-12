from __future__ import annotations

import argparse
import os.path
from typing import Generator

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def adjacent(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            yield x+i, y+j


def compute(s: str) -> int:
    data = {}
    for i, line in enumerate(s.split()):
        for j, number in enumerate(line):
            data[(i, j)] = int(number)

    flashes = 0
    for _ in range(100):
        todo = []

        for (x, y), n in data.items():
            data[(x, y)] += 1
            if data[(x, y)] > 9:
                todo.append((x, y))

        while todo:
            pt = todo.pop()
            if data[pt] == 0:
                continue

            data[pt] = 0
            flashes += 1

            for other in adjacent(*pt):
                if other in data and data[other] != 0:
                    data[other] += 1
                    if data[other] > 9:
                        todo.append(other)

    return flashes


INPUT_S = '''\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 1656),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
