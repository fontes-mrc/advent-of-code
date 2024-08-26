import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

from collections import defaultdict

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input(2023, 7)


LETTER_CARDS = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
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


@aoc_eval
def resolve():
    scores_and_bids = []
    for row in INPUT.splitlines():
        cards, bid = row.split(" ")
        parsed_cards: list[int] = []
        hand: dict[int, int] = defaultdict(int)

        for card in cards:
            parsed_card = int(LETTER_CARDS.get(card, card))
            parsed_cards.append(parsed_card)
            hand[parsed_card] += 1

        joker_count = hand.pop(1, 0)
        sorted_hand = list(sorted(hand.values(), reverse=True))
        if len(sorted_hand) > 0:
            sorted_hand[0] += joker_count
        else:
            sorted_hand.append(joker_count)

        hand_score = HAND_SCORES[tuple(sorted_hand)]
        score = tuple([hand_score] + parsed_cards)
        scores_and_bids.append((score, int(bid)))

    scores_and_bids.sort()

    return sum([s[1] * (i + 1) for i, s in enumerate(scores_and_bids)])


if __name__ == "__main__":
    print(resolve())
