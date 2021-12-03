from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    count = {'0': 0, '1': 0}
    for line in lines:
        bits = len(line)
        indBits = [dict(count) for _ in range(bits)]
        break
    for line in lines:
        for i, char in enumerate(line):
            indBits[i][char] += 1

    var, bar = [], []
    for i in range(bits):
        if indBits[i]['0'] > indBits[i]['1']:
            var.append(0)
            bar.append(1)
        else:
            var.append(1)
            bar.append(0)

    print(var)
    print(bar)
    count1 = int("".join(str(x) for x in var), 2)
    count2 = int("".join(str(x) for x in bar), 2)

    return count1 * count2


INPUT_S = '''\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 198),
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
