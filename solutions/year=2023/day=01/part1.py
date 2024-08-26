import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 1)


@aoc_eval
def resolve():
    return sum(
        [
            10 * int(next(filter(str.isdigit, row)))
            + int(next(filter(str.isdigit, row[::-1])))
            for row in INPUT.split("\n")
        ]
    )


if __name__ == "__main__":
    print(resolve())
