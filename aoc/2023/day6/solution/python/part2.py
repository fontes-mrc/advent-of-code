from pathlib import Path

input_path = Path(__file__).parent.parent.parent / "input.txt"
input_ = input_path.read_text()


def resolve(input_: str) -> int:
    time, dist = map(
        lambda x: int(x.split(":")[1].replace(" ", "")), input_.splitlines()
    )
    acc = int((time - (time**2 - 4 * dist) ** 0.5) / 2) + 1
    return time - 2 * acc + 1


print(resolve(input_))
