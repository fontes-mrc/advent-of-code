import pathlib


def get_input() -> list:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        return f.readlines()


def replace_numbers(input: str) -> str:
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
        lidx = input.find(numbers[i])
        ridx = input.rfind(numbers[i])

        if lidx != -1:
            replaces[i] = (lidx, ridx)

    for number, indexes in replaces.items():
        lidx, ridx = indexes
        input = input[:lidx] + str(number) + input[lidx + 1 :]
        input = input[:ridx] + str(number) + input[ridx + 1 :]

    return input


def main() -> None:
    inputs = get_input()
    n = 0

    for input in inputs:
        input = replace_numbers(input)
        left_ok = False
        right_ok = False

        for i in range(len(input)):
            left = input[i]
            right = input[-(i + 1)]

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
