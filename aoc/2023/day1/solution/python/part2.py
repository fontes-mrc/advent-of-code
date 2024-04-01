from pathlib import Path
import re

input_path = Path(__file__).parent.parent.parent / "input.txt"
input_ = input_path.read_text()


def resolve(input_: str) -> int:
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    remap = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    score = 0

    for row in input_.splitlines():
        matches = re.findall(pattern, row)

        if len(matches) > 0:
            score += int(remap.get(matches[0], matches[0])) * 10
            score += int(remap.get(matches[-1], matches[-1]))

    return score


print(resolve(input_))
