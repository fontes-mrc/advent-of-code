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


def calculate_part_1(input_: list[str]) -> int:
    card_scores = {}
    for row in input_:
        score = 0
        card_id = int(trim(row.split(":")[0]).split(" ")[1])
        numbers = [trim(i).split(" ") for i in row.split(":")[1].strip().split("|")]
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


def calculate_part_2(input_: list[str]) -> int:
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

    for i in range(len(input_)):
        score += process_item(input_, i)

    return score


def main() -> None:
    input_ = get_input()
    print(calculate_part_1(input_))
    print(calculate_part_2(input_))


if __name__ == "__main__":
    main()
