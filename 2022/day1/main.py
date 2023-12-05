import pathlib


def get_input() -> list:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        return f.readlines()


def main() -> None:
    input_: list[str] = get_input()
    elves = []
    elf = 0

    for row in input_:
        number = row.replace("\n", "")
        if number != "":
            elf += int(number)
        else:
            elves.append(elf)
            elf = 0

    # part 1
    print(max(elves))

    # part 2
    elves.sort()
    print(sum(elves[-3:]))


if __name__ == "__main__":
    main()
