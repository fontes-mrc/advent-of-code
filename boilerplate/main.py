"""
================================================================================
Advent of Code 20xx
...
================================================================================
"""

import pathlib


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def part1(input_: list[str]) -> int:
    score = 0
    for row in input_:
        ...
    return score


def part2(input_: list[str]) -> int:
    score = 0
    for row in input_:
        ...
    return score


def main() -> None:
    input_ = get_input()
    print(part1(input_))
    print(part2(input_))


if __name__ == "__main__":
    main()
