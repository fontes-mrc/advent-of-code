import re
from pathlib import Path

input_path = Path(__file__).parent.parent.parent / "input.txt"
input_ = input_path.read_text()


def count_matches(entry: str) -> int:
    left, right = entry.split("|")
    matches = 0
    winners = set(map(int, re.findall(r"\d+(?= )", left)))
    for i in map(int, re.findall(r"\d+", right)):
        if i in winners:
            matches += 1
    return matches


def resolve(input_: str) -> int:
    matches = [count_matches(row) for row in input_.splitlines()]
    occurences = [1] * len(matches)
    for i, match in enumerate(matches):
        for j in range(1, match + 1):
            occurences[i + j] += occurences[i]

    return sum(occurences)


print(resolve(input_))
