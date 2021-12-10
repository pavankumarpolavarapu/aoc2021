# https://www.youtube.com/watch?v=IgOEwxXIoKU
from __future__ import annotations

import argparse
import os.path
from collections import defaultdict
from typing import Generator

import pytest

from support import timing
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def adjacent(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x, y-1
    yield x, y+1
    yield x+1, y
    yield x-1, y


def compute(s: str) -> int:
    data = defaultdict(lambda: 9)
    for i, row in enumerate(s.split()):
        for j, column in enumerate(row):
            data[(i, j)] = int(column)

    total = 0
    minimas = []
    for (x, y), n in data.items():
        if all(data.get(point, 9) > n for point in adjacent(x, y)):
            total += n + 1
            minimas.append((x, y))

    basins = []
    for x, y in minimas:
        seen = set()
        todo = [(x, y)]

        while todo:
            x, y = todo.pop()
            seen.add((x, y))

            for point in adjacent(x, y):
                if point not in seen and data.get(point, 9) != 9:
                    todo.append(point)

        basins.append(len(seen))

    basins.sort()
    return (basins[-1] * basins[-2] * basins[-3])


INPUT_S = '''\
2199943210
3987894921
9856789892
8767896789
9899965678
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 1134),
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
