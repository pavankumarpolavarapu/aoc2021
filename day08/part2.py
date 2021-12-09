from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()

    count: int = 0
    for line in lines:
        display, line = line.split(' | ')
        words = [''.join(sorted(v)) for v in display.split()]
        lengths = [len(v) for v in words]
        mapped: dict[str, int] = {}
        for word in words:
            length = len(word)
            if (length == 2):
                mapped[word] = 1
            elif (length == 3):
                mapped[word] = 7
            elif (length == 4):
                mapped[word] = 4
            elif (length == 7):
                mapped[word] = 8

        wa: str = ''
        wb: str = ''
        wc: str = ''
        wd: str = ''
        we: str = ''
        wf: str = ''
        wg: str = ''
        wa = next(
            iter(set(sorted(set(words[lengths.index(3)]) -
                            set(words[lengths.index(2)])))))
        bd = set(sorted(set(words[lengths.index(4)]
                            ) - set(words[lengths.index(3)])))
        cf = set(sorted(set(words[lengths.index(2)])))
        eg = set(sorted(set(words[lengths.index(7)]
                            ) - set(wa) - set(bd) - set(cf)))

        for word in words:
            if len(word) == 6:
                cordore = set(sorted(set(words[lengths.index(7)]) - set(word)))
                if len(bd - cordore) == 1:
                    wb = next(iter(bd - cordore))
                elif len(cf - cordore) == 1:
                    wf = next(iter(cf - cordore))
                elif len(eg - cordore) == 1:
                    wg = next(iter(eg - cordore))

        we = next(iter(eg - set(wg)))
        wd = next(iter(bd - set(wb)))
        wc = next(iter(cf - set(wf)))

        mapped[''.join(sorted(wa + wb + wc + we + wf + wg))] = 0
        mapped[''.join(sorted(wa + wc + wd + we + wg))] = 2
        mapped[''.join(sorted(wa + wc + wd + wf + wg))] = 3
        mapped[''.join(sorted(wa + wb + wd + wf + wg))] = 5
        mapped[''.join(sorted(wa + wb + wd + we + wf + wg))] = 6
        mapped[''.join(sorted(wa + wb + wc + wd + wf + wg))] = 9

        m = 1000
        for word in line.split():
            try:
                count += mapped[''.join(sorted(word))] * m
                m = int(m / 10)
            except(KeyError):
                print(words)
                print(line)
                print(word)
                return 1

    return count


INPUT_S = '''\
gbcead cfgaeb beadf adb egafd fbeac dbfegca fdaceb dbfc bd | \
dfcb gedaf dcfb bcfdea
'''

# abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg | \
#        cadfg bdcf abcefg abcefg
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | \
#        cdfeb fcadb cdfeb cdbaf


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 3400),
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
