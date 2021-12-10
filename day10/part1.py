from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    matches = {'}': '{', ']': '[', ')': '(', '>': '<'}
    open_chars = ('{', '[', '(', '<')
    points = 0
    for line in lines:
        stack: list[str] = []
        for char in line:
            if len(stack) != 0:
                if char in open_chars:
                    stack.append(char)
                else:
                    if matches[char] != stack[-1]:
                        if char == ')':
                            points += 3
                        elif char == ']':
                            points += 57
                        elif char == '}':
                            points += 1197
                        elif char == '>':
                            points += 25137

                        break
                    else:
                        _ = stack.pop()
            else:
                stack.append(char)

    return points


INPUT_S = '''\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 26397),
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
