import pathlib
import re


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def trim(s: str) -> str:
    s = re.sub(" +", " ", s)
    return s.strip()


def calculate_part_1(inputs: list[str]) -> int:
    card_scores = {}
    for input in inputs:
        score = 0
        card_id = int(trim(input.split(":")[0]).split(" ")[1])
        numbers = [trim(i).split(" ") for i in input.split(":")[1].strip().split("|")]
        winners = [int(n) for n in numbers[0]]
        mine = [int(n) for n in numbers[1]]

        for m in mine:
            if m in winners:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        card_scores[card_id] = score

    score = sum(card_scores.values())
    return score


def calculate_part_2(inputs: list[str]) -> int:
    score = 0

    def process_item(inputs: list[str], i: int) -> int:
        numbers = [
            trim(j).split(" ") for j in inputs[i].split(":")[1].strip().split("|")
        ]
        winners = [int(n) for n in numbers[0]]
        mine = [int(n) for n in numbers[1]]

        matches = []
        j = 1
        for m in mine:
            if m in winners:
                matches.append(i + j)
                j += 1

        count = 1
        for match in matches:
            count += process_item(inputs, match)

        return count

    for i in range(len(inputs)):
        score += process_item(inputs, i)

    return score


def main() -> None:
    inputs = get_input()
    print(calculate_part_1(inputs))
    print(calculate_part_2(inputs))


if __name__ == "__main__":
    main()
