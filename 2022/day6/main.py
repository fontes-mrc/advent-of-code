import pathlib


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def calculate_part_1(input_: list[str]) -> int:
    size = 4
    for i in range(len(input_[0]) - (size - 1)):
        if len(set(input_[0][i : i + size])) == size:
            return i + size


def calculate_part_2(input_: list[str]) -> int:
    size = 14
    for i in range(len(input_[0]) - (size - 1)):
        if len(set(input_[0][i : i + size])) == size:
            return i + size


def main() -> None:
    input_ = get_input()
    print(calculate_part_1(input_))
    print(calculate_part_2(input_))


if __name__ == "__main__":
    main()
