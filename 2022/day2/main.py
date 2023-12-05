import pathlib


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def calculate_part_1(input_: list[str]) -> int:
    score = 0

    remap = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }

    elem = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }

    matchup = {
        "rock": {
            "rock": 3,
            "paper": 6,
            "scissors": 0,
        },
        "paper": {
            "rock": 0,
            "paper": 3,
            "scissors": 6,
        },
        "scissors": {
            "rock": 6,
            "paper": 0,
            "scissors": 3,
        },
    }

    for row in input_:
        op = remap[row.split(" ")[0]]
        me = remap[row.split(" ")[1]]

        score += matchup[op][me]
        score += elem[me]

    return score


def calculate_part_2(input_: list[str]) -> int:
    score = 0

    remap = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }

    decisions = {
        "lose": 0,
        "draw": 3,
        "win": 6,
    }

    elem = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }

    matchup = {
        "rock": {
            "lose": "scissors",
            "draw": "rock",
            "win": "paper",
        },
        "paper": {
            "lose": "rock",
            "draw": "paper",
            "win": "scissors",
        },
        "scissors": {
            "lose": "paper",
            "draw": "scissors",
            "win": "rock",
        },
    }

    for row in input_:
        op = remap[row.split(" ")[0]]
        decision = remap[row.split(" ")[1]]
        me = matchup[op][decision]

        score += decisions[decision]
        score += elem[me]

    return score


def main() -> None:
    input_ = get_input()
    print(calculate_part_1(input_))
    print(calculate_part_2(input_))


if __name__ == "__main__":
    main()
