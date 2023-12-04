import pathlib


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def calculate_part_1(inputs: list[str]) -> int:
    size = 4
    for i in range(len(inputs[0]) - (size - 1)):
        if len(set(inputs[0][i : i + size])) == size:
            return i + size


def calculate_part_2(inputs: list[str]) -> int:
    size = 14
    for i in range(len(inputs[0]) - (size - 1)):
        if len(set(inputs[0][i : i + size])) == size:
            return i + size


def main() -> None:
    inputs = get_input()
    print(calculate_part_1(inputs))
    print(calculate_part_2(inputs))


if __name__ == "__main__":
    main()
