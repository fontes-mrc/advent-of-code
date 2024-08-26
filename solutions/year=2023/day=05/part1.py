import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

import re

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 5)


@aoc_eval
def resolve():
    segments = INPUT.split("\n\n")
    seeds = re.findall(r"\d+", segments[0])

    min_location = float("inf")
    for x in map(int, seeds):
        for seg in segments[1:]:
            for conversion in re.findall(r"(\d+) (\d+) (\d+)", seg):
                destination, start, delta = map(int, conversion)
                if x in range(start, start + delta):
                    x += destination - start
                    break

        min_location = min(x, min_location)

    return int(min_location)


if __name__ == "__main__":
    print(resolve())
