import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

import re
from math import prod

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 6)


def trim(s: str) -> str:
    s = re.sub(" +", " ", s)
    return s.strip()


@aoc_eval
def resolve():
    times = [int(i) for i in trim(INPUT.splitlines()[0].split(":")[1]).split(" ")]
    dists = [int(i) for i in trim(INPUT.splitlines()[1].split(":")[1]).split(" ")]

    results = []
    for time, dist in zip(times, dists):
        acc = int((time - (time**2 - 4 * dist) ** 0.5) / 2) + 1
        results.append(time - 2 * acc + 1)

    return prod(results)


if __name__ == "__main__":
    print(resolve())
