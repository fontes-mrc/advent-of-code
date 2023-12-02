import pathlib
import re
from functools import reduce


def get_input() -> list:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        return f.readlines()


def split_game(game: str) -> tuple[int, list[list[str]]]:
    game_id = int(game.split(":")[0].split(" ")[1])
    sets = [item.strip().split(" ") for item in re.split("; |, ", game.split(":")[1])]
    return game_id, sets


def calculate_part_1(inputs: str) -> int:
    n = 0
    max_ = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    for input in inputs:
        game_id, sets = split_game(input)
        valid_game = True

        for set in sets:
            qtd = int(set[0])
            color = set[1]

            for ref in ["red", "green", "blue"]:
                if color == ref and qtd > max_[ref]:
                    valid_game = False
                    break

        n += game_id if valid_game else 0
    return n


def calculate_part_2(inputs: str) -> int:
    n = 0

    for input in inputs:
        max_ = {}
        _, sets = split_game(input)

        for set in sets:
            qtd = int(set[0])
            color = set[1]
            max_[color] = max(max_.get(color, 0), qtd)

        power_ = reduce((lambda x, y: x * y), max_.values())
        n += power_

    return n


def main() -> None:
    inputs = get_input()
    print(calculate_part_1(inputs))
    print(calculate_part_2(inputs))


if __name__ == "__main__":
    main()
