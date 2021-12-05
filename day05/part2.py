from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    chart: dict[tuple[int, int], int] = {}
    for line in lines:
        l, _, r = line.partition('->')
        x1, y1 = map(int, l.split(","))
        x2, y2 = map(int, r.split(","))

        if (x1 == x2):
            for j in range(min(y1, y2), max(y1, y2) + 1):
                chart[(x1, j)] = 1 if (
                    x1, j) not in chart else chart[(x1, j)] + 1

        if (y1 == y2):
            for j in range(min(x1, x2), max(x1, x2) + 1):
                chart[(j, y1)] = 1 if (
                    j, y1) not in chart else chart[(j, y1)] + 1

        elif (abs(x1-x2) == abs(y1-y2)):
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            while True:
                chart[(x1, y1)] = 1 if (
                    x1, y1) not in chart else chart[(x1, y1)] + 1
                if (x1, y1) == (x2, y2):
                    break
                x1 += dx
                y1 += dy

    return len([entry for entry in chart if chart[(entry)] > 1])


INPUT_S = '''\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 12),
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
