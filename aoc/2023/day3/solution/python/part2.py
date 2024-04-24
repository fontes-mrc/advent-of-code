import math
import re
from pathlib import Path

input_path = Path(__file__).parent.parent.parent / "input.txt"
input_ = input_path.read_text()


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


def resolve(input_: str) -> int:
    numbers = get_numbers(input_)

    found: list[int] = []
    for y, line in enumerate(input_.splitlines()):
        for x, char in enumerate(line):
            if char == "*":
                neighbors = get_neighbors(x, y, numbers)
                if len(neighbors) == 2:
                    found.append(math.prod(neighbors))
    return sum(found)


print(resolve(input_))
