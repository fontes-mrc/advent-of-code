import pathlib


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def calculate_part_1(inputs: list[str]) -> int:
    score = 0
    for input in inputs:
        l = [int(i) for i in input.split(",")[0].split("-")]
        r = [int(i) for i in input.split(",")[1].split("-")]

        if l[0] == r[0]:
            score += 1

        else:
            if l[0] > r[0]:
                l, r = r, l

            if l[1] >= r[1]:
                score += 1

    return score


def calculate_part_2(inputs: list[str]) -> int:
    score = 0
    for input in inputs:
        l = [int(i) for i in input.split(",")[0].split("-")]
        r = [int(i) for i in input.split(",")[1].split("-")]

        if l[0] == r[0] or l[1] == r[1]:
            score += 1

        else:
            if l[0] > r[0]:
                l, r = r, l

            if l[1] >= r[0]:
                score += 1

    return score


def main() -> None:
    inputs = get_input()
    print(calculate_part_1(inputs))
    print(calculate_part_2(inputs))


if __name__ == "__main__":
    main()
