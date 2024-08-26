import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

from math import comb

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 9)


@aoc_eval
def resolve():
    score = 0
    for row in INPUT.splitlines():
        seq = list(map(int, row.split()))
        len_seq = len(seq)
        next_num = 0
        for i, n in enumerate(seq):
            next_num += n * comb(len_seq, i) * (-1) ** (len_seq - 1 - i)

        score += next_num
    return score


if __name__ == "__main__":
    print(resolve())
