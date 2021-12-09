from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()

    signal = {'abcefg': (0, 5), 'cf': (1, 2),
              'acdeg': (2, 5), 'acdfg': (3, 5),
              'bcdf': (4, 4), 'abdfg': (5, 5),
              'abdefg': (6, 6), 'acf': (7, 3),
              'abcdefg': (8, 7), 'abcdfg': (9, 6)}
    count: int = 0
    for line in lines:
        _, line = line.split(' | ')
        words = line.split()
        for word in words:
            for k, v in signal.items():
                if len(word) == v[1] and v[0] in (1, 4, 7, 8):
                    count += 1
    return count


INPUT_S = '''\
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |\
cdfeb fcadb cdfeb cdbaf
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 0),
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
