from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    fishes = [int(s) for s in s.split(',')]

    days = 256
    counts = [0 for _ in range(9)]

    for fish in fishes:
        counts[fish] += 1

    for day in range(days):
        new_born = counts[0]

        counts = counts[1:]
        counts.append(0)
        counts[6] += new_born
        counts[8] = new_born

    return sum(counts)


INPUT_S = '''\
3,4,3,1,2
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 26984457539),
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
