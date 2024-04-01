from pathlib import Path

input_path = Path(__file__).parent.parent.parent / "input.txt"
input_ = input_path.read_text()


def resolve(input_: str) -> int:
    return sum(
        [
            10 * int(next(filter(str.isdigit, row)))
            + int(next(filter(str.isdigit, row[::-1])))
            for row in input_.split("\n")
        ]
    )


print(resolve(input_))
