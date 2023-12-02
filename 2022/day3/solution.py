import pathlib

l = list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


# avoid the use of set.intersection
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


def calculate_part_1(inputs: list[str]) -> int:
    score = 0
    for input in inputs:
        left = list(input[: int(len(input) / 2)])
        right = list(input[int(len(input) / 2) :])

        inter = get_intersection(left, right)
        score += l.index(inter[0])

    return score


def calculate_part_2(inputs: list[str]) -> int:
    score = 0
    for i in range(0, len(inputs), 3):
        row1 = inputs[i]
        row2 = inputs[i + 1]
        row3 = inputs[i + 2]

        combo1 = get_intersection(list(row1), list(row2))
        inter = get_intersection(combo1, list(row3))
        score += l.index(inter[0])

    return score


def main():
    inputs = get_input()
    print(calculate_part_1(inputs))
    print(calculate_part_2(inputs))


if __name__ == "__main__":
    main()
