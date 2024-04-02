from pathlib import Path
from collections import defaultdict

input_path = Path(__file__).parent.parent.parent / "input.txt"
input_ = input_path.read_text()


LETTER_CARDS = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
}

HAND_SCORES = {
    (5,): 7,
    (4, 1): 6,
    (3, 2): 5,
    (3, 1, 1): 4,
    (2, 2, 1): 3,
    (2, 1, 1, 1): 2,
    (1, 1, 1, 1, 1): 1,
}


def resolve(input_: str) -> int:
    scores_and_bids = []
    for row in input_.splitlines():
        cards, bid = row.split(" ")
        parsed_cards: list[int] = []
        hand: dict[int, int] = defaultdict(int)

        for card in cards:
            parsed_card = int(LETTER_CARDS.get(card, card))
            parsed_cards.append(parsed_card)
            hand[parsed_card] += 1

        sorted_hand = tuple(sorted(hand.values(), reverse=True))

        hand_score = HAND_SCORES[sorted_hand]
        score = tuple([hand_score] + parsed_cards)
        scores_and_bids.append((score, int(bid)))

    scores_and_bids.sort()

    return sum([s[1] * (i + 1) for i, s in enumerate(scores_and_bids)])


print(resolve(input_))
