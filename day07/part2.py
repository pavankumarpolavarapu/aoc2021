from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    data = [int(line) for line in s.split(',')]

    mean = round(sum(data) / len(data))
    mindist = 999999999999999999
    for i in range(abs(round(mean - 10)), round(mean + 10)):
        cumdist = 0
        for j in data:
            diff = abs(i-j)
            dist = (diff * (diff+1)) / 2
            cumdist += int(dist)
            if i == 5:
                print(dist)

        if cumdist < mindist:
            mindist = cumdist
    return(mindist)


INPUT_S = '''\
16,1,2,0,4,2,7,1,2,14
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 168),
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
