import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

import math
import re

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 3)


def get_numbers(input_: str) -> dict[tuple[int, int], int]:
    numbers = {}
    for y, line in enumerate(input_.splitlines()):
        for match in re.finditer(r"\d+", line):
            number = int(match.group())
            x1 = match.start()
            x2 = match.end() - 1
            for x in range(x1, x2 + 1):
                numbers[(x, y)] = number

    return numbers


def get_neighbors(x: int, y: int, numbers: dict[tuple[int, int], int]) -> list[int]:
    found = set()
    for x_ in range(x - 1, x + 2):
        for y_ in range(y - 1, y + 2):
            if (x_, y_) in numbers:
                found.update([numbers[(x_, y_)]])
    return list(found)


@aoc_eval
def resolve():
    numbers = get_numbers(INPUT)

    found: list[int] = []
    for y, line in enumerate(INPUT.splitlines()):
        for x, char in enumerate(line):
            if char == "*":
                neighbors = get_neighbors(x, y, numbers)
                if len(neighbors) == 2:
                    found.append(math.prod(neighbors))
    return sum(found)


if __name__ == "__main__":
    print(resolve())
