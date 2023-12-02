import pathlib


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def calculate_part_1(inputs: list[str]) -> int:
    score = 0
    for input in inputs:
        ...
    return score


def calculate_part_2(inputs: list[str]) -> int:
    score = 0
    for input in inputs:
        ...
    return score


def main() -> None:
    inputs = get_input()
    print(calculate_part_1(inputs))
    print(calculate_part_1(inputs))


if __name__ == "__main__":
    main()
