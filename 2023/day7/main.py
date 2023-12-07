import pathlib
from collections import defaultdict


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def move_char_to_end(string: str, char: str) -> str:
    count = string.count(char)
    string = string.replace(char, "")
    return f"{string}{''.join([char] * count)}"


def get_score(cards: str) -> tuple:
    letter_cards = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
    }
    hand_scores = {
        (5,): 7,
        (4, 1): 6,
        (3, 2): 5,
        (3, 1, 1): 4,
        (2, 2, 1): 3,
        (2, 1, 1, 1): 2,
        (1, 1, 1, 1, 1): 1,
    }

    hand = defaultdict(int)
    parsed_cards = []

    for card in cards:
        parsed_card = letter_cards.get(card, card)
        parsed_cards.append(parsed_card)
        hand[parsed_card] += 1

    sorted_hand = tuple(sorted(hand.values(), reverse=True))

    hand_score = hand_scores[sorted_hand]
    score = tuple([hand_score] + [int(c) for c in parsed_cards])

    return score


def get_score_with_joker(cards: str) -> tuple:
    letter_cards = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 0,
        "T": 10,
    }
    hand_scores = {
        (5,): 7,
        (4, 1): 6,
        (3, 2): 5,
        (3, 1, 1): 4,
        (2, 2, 1): 3,
        (2, 1, 1, 1): 2,
        (1, 1, 1, 1, 1): 1,
    }

    hand = defaultdict(int)
    for card in move_char_to_end(cards, "J"):
        parsed_card = letter_cards.get(card, card)
        if card != "J":
            hand[parsed_card] += 1
        else:
            sub_sort = sorted(hand.items(), key=(lambda x: x[1]), reverse=True)
            hand[sub_sort[0][0]] += 1

    parsed_cards = [letter_cards.get(c, c) for c in cards]
    sorted_hand = tuple(sorted(hand.values(), reverse=True))

    hand_score = hand_scores[sorted_hand]
    score = tuple([hand_score] + [int(c) for c in parsed_cards])

    return score


def calculate_part_1(input_: list[str]) -> int:
    scores_and_bids = []
    for row in input_:
        cards, bid = row.split(" ")
        score = get_score(cards)
        scores_and_bids.append((score, int(bid)))

    scores_and_bids.sort()

    return sum([s[1] * (i + 1) for i, s in enumerate(scores_and_bids)])


def calculate_part_2(input_: list[str]) -> int:
    scores_and_bids = []
    for row in input_:
        cards, bid = row.split(" ")
        score = get_score_with_joker(cards)
        scores_and_bids.append((score, int(bid)))

    scores_and_bids.sort()

    return sum([s[1] * (i + 1) for i, s in enumerate(scores_and_bids)])


def main() -> None:
    input_ = get_input()
    print(calculate_part_1(input_))
    print(calculate_part_2(input_))


if __name__ == "__main__":
    main()
