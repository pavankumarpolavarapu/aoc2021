from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    numbers = [[int(point) for point in line] for line in s.splitlines()]
    points = []
    for i, row in enumerate(numbers):
        for j, number in enumerate(row):
            try:
                left = 10 ** 9 if (j-1) < 0 else numbers[i][j-1]
                right = 10 ** 9 if (j+2) > len(row) else numbers[i][j+1]
                down = 10 ** 9 if (i+2) > len(numbers) else numbers[i+1][j]
                up = 10 ** 9 if (i-1) < 0 else numbers[i-1][j]

                current = number
                if current >= left:
                    continue
                elif current >= right:
                    continue
                elif current >= up:
                    continue
                elif current >= down:
                    continue
                else:
                    points.append(current)
            except IndexError:
                return -1
    return sum(points) + len(points)


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
        (INPUT_S, 15),
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
