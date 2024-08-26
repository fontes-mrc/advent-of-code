import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 6)


@aoc_eval
def resolve():
    time, dist = map(
        lambda x: int(x.split(":")[1].replace(" ", "")), INPUT.splitlines()
    )
    acc = int((time - (time**2 - 4 * dist) ** 0.5) / 2) + 1
    return time - 2 * acc + 1


if __name__ == "__main__":
    print(resolve())
