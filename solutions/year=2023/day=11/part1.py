import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

from itertools import combinations

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 11)


def empty_spaces(input_: list[str]) -> dict[str, list[int]]:
    spaces = {"x": [], "y": []}

    for i, row in enumerate(input_):
        if len(set(row)) == 1:
            spaces["y"].append(i)

    for i in range(len(input_[0])):
        if len(set([r[i] for r in input_])) == 1:
            spaces["x"].append(i)

    return spaces


def offset(
    spaces: dict[str, list[int]],
    x: int,
    y: int,
    n: int = 1,
) -> tuple[int, int]:
    x_offset = sum(i < x for i in spaces["x"]) * n
    y_offset = sum(i < y for i in spaces["y"]) * n

    return (x + x_offset, y + y_offset)


def dist(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p2[1] - p1[1]) + abs(p2[0] - p1[0])


@aoc_eval
def resolve():
    map_ = INPUT.splitlines()

    spaces = empty_spaces(map_)
    points = []

    for y, row in enumerate(map_):
        for x, char in enumerate(row):
            if char == "#":
                points.append(offset(spaces, x, y))

    dists = [dist(p1, p2) for p1, p2 in combinations(points, 2)]
    return sum(dists)


if __name__ == "__main__":
    print(resolve())
