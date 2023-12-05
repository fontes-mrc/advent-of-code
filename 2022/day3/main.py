import pathlib

l = list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


# avoid the use of set.intersection for pure practice
def get_intersection(
    left: list[str],
    right: list[str],
) -> list[str]:
    left_hash = set(left)
    inter = []
    for c in right:
        if c in left_hash:
            inter.append(c)

    return inter


def calculate_part_1(input_: list[str]) -> int:
    score = 0
    for row in input_:
        left = list(row[: int(len(row) / 2)])
        right = list(row[int(len(row) / 2) :])

        inter = get_intersection(left, right)
        score += l.index(inter[0])

    return score


def calculate_part_2(input_: list[str]) -> int:
    score = 0
    for i in range(0, len(input_), 3):
        row1 = input_[i]
        row2 = input_[i + 1]
        row3 = input_[i + 2]

        combo1 = get_intersection(list(row1), list(row2))
        inter = get_intersection(combo1, list(row3))
        score += l.index(inter[0])

    return score


def main():
    input_ = get_input()
    print(calculate_part_1(input_))
    print(calculate_part_2(input_))


if __name__ == "__main__":
    main()
