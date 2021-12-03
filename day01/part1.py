from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    count = 0
    temp = 3333333333
    for n in numbers:
        if n > temp:
            count = count + 1
        temp = n

    print(count)
    return count

    lines = s.splitlines()
    for line in lines:
        pass
    # TODO: implement solution here!
    return 0


INPUT_S = '''\
169
150
158
163
167
151
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 3),
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
