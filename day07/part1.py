from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    data = [int(line) for line in s.split(',')]

    mindist = 99999999999999999
    for i in range(max(data)):
        data = [j - 1 for j in data]
        dist = sum(abs(j) for j in data)
        if dist < mindist:
            mindist = dist

    return(mindist)


INPUT_S = '''\
16,1,2,0,4,2,7,1,2,14
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 37),
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
