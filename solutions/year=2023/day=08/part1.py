import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 8)


def next_command(commands: list[str]) -> str:
    next_ = commands.pop(0)
    commands.append(next_)
    return next_


def get_commands_and_elements(
    input_: str,
) -> tuple[list[str], dict[str, dict[str, str]]]:
    splitted = input_.splitlines()
    commands = list(splitted[0])
    elements = {i[:3]: {"L": i[7:10], "R": i[12:15]} for i in splitted[2:]}
    return commands, elements


@aoc_eval
def resolve():
    commands, elements = get_commands_and_elements(INPUT)

    moves = 0
    key = "AAA"
    while key != "ZZZ":
        command = next_command(commands)
        key = elements[key][command]
        moves += 1

    return moves


if __name__ == "__main__":
    print(resolve())
