import pathlib
import re
from functools import reduce


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def trim(s: str) -> str:
    s = re.sub(" +", " ", s)
    return s.strip()


def calculate_part_1(input_: list[str]) -> int:
    times = [int(i) for i in trim(input_[0].split(":")[1]).split(" ")]
    dists = [int(i) for i in trim(input_[1].split(":")[1]).split(" ")]

    wins = []
    for t, d in zip(times, dists):
        win = 0
        for i in range(t):
            dist = (t - i) * i
            if dist > d:
                win += 1

        wins.append(win)

    return reduce((lambda x, y: x * y), wins)


def calculate_part_2(input_: list[str]) -> int:
    time = int(input_[0].split(":")[1].replace(" ", ""))
    dist = int(input_[1].split(":")[1].replace(" ", ""))

    i = 0
    while (time - i) * i <= dist:
        i += 1

    return time - (i * 2) + 1


def main() -> None:
    input_ = get_input()
    print(calculate_part_1(input_))
    print(calculate_part_2(input_))


if __name__ == "__main__":
    main()
