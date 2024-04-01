from pathlib import Path
import re
from math import prod


input_path = Path(__file__).parent.parent.parent / "input.txt"
input_ = input_path.read_text()


def trim(s: str) -> str:
    s = re.sub(" +", " ", s)
    return s.strip()


def resolve(input_: str) -> int:
    times = [int(i) for i in trim(input_.splitlines()[0].split(":")[1]).split(" ")]
    dists = [int(i) for i in trim(input_.splitlines()[1].split(":")[1]).split(" ")]

    results = []
    for time, dist in zip(times, dists):
        acc = int((time - (time**2 - 4 * dist) ** 0.5) / 2) + 1
        results.append(time - 2 * acc + 1)

    return prod(results)


print(resolve(input_))
