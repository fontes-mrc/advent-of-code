from pathlib import Path
import re

input_path = Path(__file__).parent.parent.parent / "input.txt"
input_ = input_path.read_text()


def resolve(input_: str) -> int:
    segments = input_.split("\n\n")
    seeds = re.findall(r"\d+", segments[0])

    min_location = float("inf")
    for x in map(int, seeds):
        for seg in segments[1:]:
            for conversion in re.findall(r"(\d+) (\d+) (\d+)", seg):
                destination, start, delta = map(int, conversion)
                if x in range(start, start + delta):
                    x += destination - start
                    break

        min_location = min(x, min_location)

    return int(min_location)


print(resolve(input_))
