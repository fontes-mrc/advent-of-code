import pathlib
from math import lcm


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def next_command(commands: list[str]) -> str:
    next_ = commands.pop(0)
    commands.append(next_)
    return next_


def calculate_part_1(input_: list[str]) -> int:
    commands = list(input_[0])
    elements = {i[:3]: {"L": i[7:10], "R": i[12:15]} for i in input_[2:]}

    moves = 0
    key = "AAA"
    while key != "ZZZ":
        command = next_command(commands)
        key = elements[key][command]
        moves += 1

    return moves


def calculate_part_2(input_: list[str]) -> int:
    commands = list(input_[0])
    elements = {i[:3]: {"L": i[7:10], "R": i[12:15]} for i in input_[2:]}

    all_moves = []
    keys = filter((lambda x: x.endswith("A")), elements.keys())
    for key in keys:
        moves = 0
        while not key.endswith("Z"):
            command = next_command(commands)
            key = elements[key][command]
            moves += 1
        all_moves.append(moves)

    return lcm(*all_moves)


def main() -> None:
    input_ = get_input()
    print(calculate_part_1(input_))
    print(calculate_part_2(input_))


if __name__ == "__main__":
    main()
