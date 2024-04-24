from math import lcm
from pathlib import Path

input_path = Path(__file__).parent.parent.parent / "input.txt"
input_ = input_path.read_text()


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


def resolve(input_: str) -> int:
    commands, elements = get_commands_and_elements(input_)

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


print(resolve(input_))
