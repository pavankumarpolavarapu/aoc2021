from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    numbers = [int(s) for s in s.split(',')]

    days = 257
    initialset = numbers
    spawnset: list[int] = []
    for i in range(days):
        print(f'day {i} ', end='')
        if i == 1:
            initialset = [x-1 for x in initialset]
        else:
            initialset = [x-1 for x in initialset]
            if len(spawnset) != 0:
                spawnset = [x-1 for x in spawnset]

        count1 = 0
        for j, number in enumerate(initialset):
            if number == -1:
                count1 += 1
                initialset[j] = 6

        count2 = 0
        for k, number in enumerate(spawnset):
            if number == -1:
                count2 += 1
                spawnset[k] = 6

        for i in range(count1 + count2):
            spawnset.append(8)

    return(len(initialset) + len(spawnset) - count1 - count2)


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
