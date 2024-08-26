import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 10)


def parse_pipe(
    coords: tuple[int, int],
    pipe: str,
) -> dict[str, tuple[tuple[int, int], str]]:
    sumc = lambda x, y: tuple(map(sum, zip(x, y)))

    pipes = {
        "|": ("N", "S"),
        "-": ("E", "W"),
        "L": ("N", "E"),
        "J": ("N", "W"),
        "7": ("S", "W"),
        "F": ("S", "E"),
    }

    dirs = {
        "N": ((0, -1), "S"),
        "S": ((0, 1), "N"),
        "W": ((-1, 0), "E"),
        "E": ((1, 0), "W"),
        "M": ((0, 0), "M"),
    }

    if pipe in pipes:
        d1, d2 = pipes[pipe]
        return {
            d1: (sumc(coords, dirs[d2][0]), dirs[d2][1]),
            d2: (sumc(coords, dirs[d1][0]), dirs[d1][1]),
        }

    else:
        return {}


def parse_s(
    coord: tuple[int, int], map_: list[str]
) -> tuple[str, tuple[tuple[int, int], str]]:
    e_coord = (coord[0] + 1, coord[1])
    w_coord = (coord[0] - 1, coord[1])
    s_coord = (coord[0], coord[1] + 1)
    n_coord = (coord[0], coord[1] - 1)

    sides = []
    first_move = ((0, 0), "M")

    if map_[e_coord[1]][e_coord[0]] in ["-", "J", "7"]:
        sides.append("E")
        first_move = (e_coord, "W")

    if map_[w_coord[1]][w_coord[0]] in ["-", "L", "F"]:
        sides.append("W")
        first_move = (w_coord, "E")

    if map_[s_coord[1]][s_coord[0]] in ["|", "J", "L"]:
        sides.append("S")
        first_move = (s_coord, "N")

    if map_[n_coord[1]][n_coord[0]] in ["|", "F", "7"]:
        sides.append("N")
        first_move = (n_coord, "S")

    if "N" in sides and "S" in sides:
        return "|", first_move

    if "E" in sides and "W" in sides:
        return "-", first_move

    if "N" in sides and "E" in sides:
        return "L", first_move

    if "N" in sides and "W" in sides:
        return "J", first_move

    if "S" in sides and "W" in sides:
        return "7", first_move

    if "S" in sides and "E" in sides:
        return "F", first_move


def count_filled(
    points: list[tuple[int, int]],
    map_: list[str],
    new_s: str,
) -> int:
    map_cleaned = [
        ["." if (j, i) not in points else map_[i][j] for j in range(len(map_[i]))]
        for i in range(len(map_))
    ]

    map_cleaned[points[0][1]][points[0][0]] = new_s

    filled = 0
    for row in map_cleaned:
        for i, char in enumerate(row):
            if char != ".":
                continue

            intersect = 0
            corner_pipes = []
            for j in range(i + 1, len(row)):
                if row[j] in "|":
                    intersect += 1
                if row[j] in "FL":
                    corner_pipes.append(row[j])
                if (
                    len(corner_pipes) != 0
                    and row[j] == "J"
                    and corner_pipes[-1] == "F"
                    or row[j] == "7"
                    and corner_pipes[-1] == "L"
                ):
                    corner_pipes.pop(-1)
                    intersect += 1

            if intersect % 2 == 1:
                filled += 1

    return filled


@aoc_eval
def resolve():
    pipes, s = {}, ()
    map_ = INPUT.splitlines()

    for i in range(len(map_)):
        for j in range(len(map_[i])):
            coord = (j, i)
            pipe = map_[i][j]

            pipes.update({coord: parse_pipe(coord, pipe)})
            if pipe == "S":
                s = coord

    path = [s]
    new_s, move = parse_s(s, map_)
    while move:
        path.append(move[0])
        move = pipes[move[0]].get(move[1], None)

    return count_filled(path, map_, new_s)


if __name__ == "__main__":
    print(resolve())
