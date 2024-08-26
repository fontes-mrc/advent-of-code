import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

import re

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 4)


@aoc_eval
def resolve():
    score = 0
    for row in INPUT.splitlines():
        left, right = row.split("|")
        row_score = 0
        winners = set(map(int, re.findall(r"\d+(?= )", left)))
        for i in map(int, re.findall(r"\d+", right)):
            if i in winners:
                row_score *= 2
                if row_score == 0:
                    row_score = 1
        score += row_score

    return score


if __name__ == "__main__":
    print(resolve())
