import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

import re
from functools import reduce

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 2)


def parse_game(game: str) -> tuple[int, dict[str, int]]:
    game_id = int(re.findall(r"(?<=Game )\d+", game)[0])
    colors: dict[str, int] = {}
    for i in re.findall(r"\d+(?> blue| red| green)", game):
        n, color = i.split(" ")
        colors[color] = max(int(n), colors.get(color, 0))

    return game_id, colors


@aoc_eval
def resolve():
    return sum(
        reduce(lambda x, y: x * y, colors.values())
        for _, colors in map(parse_game, INPUT.splitlines())
    )


if __name__ == "__main__":
    print(resolve())
