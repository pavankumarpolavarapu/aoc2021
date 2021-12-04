from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    numbers, *boards_cc = s.split('\n\n')

    boards: list[dict[int, bool]] = [
        {int(s): False for s in board.split()} for board in boards_cc]

    for number in numbers.split(','):
        boards_copy = boards.copy()
        for c, board in enumerate(boards_copy):
            if int(number) in board:
                board[int(number)] = True
            if len(boards_copy) == 1:
                sum_of_keys = sum(int(k)
                                  for k, v in board.items() if not v)
                return sum_of_keys * int(number)

            for i in range(5):
                for j in range(5):
                    key = i * 5 + j
                    if not (list(board.values())[key]):
                        break
                else:
                    boards.remove(board)
                    break
            else:
                for i in range(5):
                    for j in range(5):
                        key = i + j * 5
                        if not (list(board.values())[key]):
                            break
                    else:
                        boards.remove(board)
                        break
    return -1


INPUT_S = '''\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 1924),
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
