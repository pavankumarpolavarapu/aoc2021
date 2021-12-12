from __future__ import annotations

import argparse
import collections
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    nodes: dict[str, list[str]] = {}
    for line in lines:
        x, y = line.split('-')
        if x in nodes:
            nodes[x].append(y)
        else:
            nodes[x] = [y]
        if y in nodes:
            nodes[y].append(x)
        else:
            nodes[y] = [x]

    todo: collections.deque[tuple[str, ...]] = collections.deque([('start',)])
    done = []
    while todo:
        path = todo.popleft()
        if path[-1] == 'end':
            done.append(path)
            continue

        for node in nodes[path[-1]]:
            if node.isupper() or node not in path:
                todo.append((*path, node))

    return len(done)


INPUT_1 = '''\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''

INPUT_2 = '''\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_1, 10),
        (INPUT_2, 19)
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
