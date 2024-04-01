from pathlib import Path
import re

input_path = Path(__file__).parent.parent.parent / "input.txt"
input_ = input_path.read_text()


def resolve(input_: str) -> int:
    score = 0
    for row in input_.splitlines():
        left, right = row.split("|")
        row_score = 0
        winners = set(map(int, re.findall(r"\d+(?= )", left)))
        for i in map(int, re.findall(r"\d+", right)):
            if i in winners:
                row_score *= 2
                if row_score == 0:
                    row_score = 1
        score += row_score

    return score


print(resolve(input_))
