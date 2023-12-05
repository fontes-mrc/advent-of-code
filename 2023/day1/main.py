import pathlib


def get_input() -> list:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        return f.readlines()


def replace_numbers(input_: str) -> str:
    numbers = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    replaces = {}
    for i in range(len(numbers)):
        lidx = input_.find(numbers[i])
        ridx = input_.rfind(numbers[i])

        if lidx != -1:
            replaces[i] = (lidx, ridx)

    for number, indexes in replaces.items():
        lidx, ridx = indexes
        input_ = input_[:lidx] + str(number) + input_[lidx + 1 :]
        input_ = input_[:ridx] + str(number) + input_[ridx + 1 :]

    return input_


def main() -> None:
    input_ = get_input()
    n = 0

    for row in input_:
        row = replace_numbers(row)
        left_ok = False
        right_ok = False

        for i in range(len(row)):
            left = row[i]
            right = row[-(i + 1)]

            if left.isdigit() and not left_ok:
                n += int(left) * 10
                left_ok = True

            if right.isdigit() and not right_ok:
                n += int(right)
                right_ok = True

            if left_ok and right_ok:
                break

    print(n)


if __name__ == "__main__":
    main()
