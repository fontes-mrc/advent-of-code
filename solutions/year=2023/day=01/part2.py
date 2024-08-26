import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

import re

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 1)


@aoc_eval
def resolve():
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    remap = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    score = 0

    for row in INPUT.splitlines():
        matches = re.findall(pattern, row)

        if len(matches) > 0:
            score += int(remap.get(matches[0], matches[0])) * 10
            score += int(remap.get(matches[-1], matches[-1]))

    return score


if __name__ == "__main__":
    print(resolve())
