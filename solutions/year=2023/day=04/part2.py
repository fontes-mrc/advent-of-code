import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

import re

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 4)


def count_matches(entry: str) -> int:
    left, right = entry.split("|")
    matches = 0
    winners = set(map(int, re.findall(r"\d+(?= )", left)))
    for i in map(int, re.findall(r"\d+", right)):
        if i in winners:
            matches += 1
    return matches


@aoc_eval
def resolve():
    matches = [count_matches(row) for row in INPUT.splitlines()]
    occurences = [1] * len(matches)
    for i, match in enumerate(matches):
        for j in range(1, match + 1):
            occurences[i + j] += occurences[i]

    return sum(occurences)


if __name__ == "__main__":
    print(resolve())
