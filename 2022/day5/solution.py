import pathlib
from collections import defaultdict
import re


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def parse_stacks(matrix: list[str]) -> dict[int, list[str]]:
    stacks = defaultdict(list)
    for row in reversed(matrix):
        for i, value in enumerate(row):
            stack_id, modulo = divmod(i - 1, 4)
            if modulo == 0 and value != " ":
                stacks[stack_id + 1].append(value)

    return dict(stacks)


def parse_order(order: str) -> tuple[int, int, int]:
    qtd = int(re.findall(r"(?<=move )\d+", order)[0])
    from_ = int(re.findall(r"(?<=from )\d+", order)[0])
    to_ = int(re.findall(r"(?<=to )\d+", order)[0])

    return qtd, from_, to_


def calculate_part_1(inputs: list[str]) -> str:
    stacks_diagram = []
    while len(inputs[0]) != 0:
        stacks_diagram.append(inputs.pop(0))
    inputs.pop(0)

    stacks = parse_stacks(stacks_diagram[:-1])
    for input in inputs:
        qtd, from_, to_ = parse_order(input)

        while qtd > 0:
            stacks[to_].append(stacks[from_].pop())
            qtd -= 1

    return "".join([s[-1] for s in stacks.values()])


def calculate_part_2(inputs: list[str]) -> str:
    stacks_diagram = []
    while len(inputs[0]) != 0:
        stacks_diagram.append(inputs.pop(0))
    inputs.pop(0)

    stacks = parse_stacks(stacks_diagram[:-1])
    for input in inputs:
        qtd, from_, to_ = parse_order(input)

        stacks[to_].extend(stacks[from_][-qtd:])
        del stacks[from_][-qtd:]

    return "".join([s[-1] for s in stacks.values()])


def main() -> None:
    inputs = get_input()
    print(calculate_part_1(inputs.copy()))
    print(calculate_part_2(inputs.copy()))


if __name__ == "__main__":
    main()
