from math import comb
from pathlib import Path

input_path = Path(__file__).parent.parent.parent / "input.txt"
input_ = input_path.read_text()


def resolve(input_: str) -> int:
    score = 0
    for row in input_.splitlines():
        seq = list(map(int, row.split()))
        len_seq = len(seq)
        next_num = 0
        for i, n in enumerate(seq):
            next_num += n * comb(len_seq, i + 1) * (-1) ** (i)

        score += next_num
    return score


print(resolve(input_))
