import pathlib
import string
from functools import reduce


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def get_ranges(
    matrix: list[str],
    i: int,
    cols: list[int],
) -> tuple[list[int], list[int]]:
    if cols[0] > 0:
        cols.insert(0, cols[0] - 1)

    if cols[-1] < (len(matrix[i]) - 1):
        cols.append(cols[-1] + 1)

    rows = [i]
    if i > 0:
        rows.insert(0, i - 1)
    if i < (len(matrix) - 1):
        rows.append(i + 1)

    return rows, cols


def is_part_number(
    matrix: list[str], rows: list[int], cols: list[int], symbols: list[str]
) -> bool:
    for r in rows:
        for c in cols:
            cell = matrix[r][c]
            if cell in symbols:
                return True

    return False


def update_gears(
    gears: dict[int, dict[int, list[int]]],
    matrix: list[str],
    rows: list[int],
    cols: list[int],
    number: int,
) -> None:
    for r in rows:
        if not gears.get(r):
            gears[r] = {}
        for c in cols:
            if matrix[r][c] == "*":
                try:
                    gears[r][c].append(number)
                except:
                    gears[r][c] = [number]
                break


def get_gear_ratios(
    gears: dict[int, dict[int, list[int]]],
) -> list[int]:
    new_values = []
    for _, sub in gears.items():
        for _, values in sub.items():
            if len(values) > 1:
                new_values.append(reduce((lambda x, y: x * y), values))

    return new_values


def calculate_part_1(inputs: list[str]) -> int:
    part_numbers: list[int] = []
    symbols = list(string.punctuation)
    symbols.remove(".")

    for i in range(len(inputs)):
        digits, cols = "", []

        for j in range(len(inputs[i])):
            char_at: str = inputs[i][j]

            if char_at.isdigit():
                digits += char_at
                cols.append(j)

            if j == (len(inputs[i]) - 1) or not char_at.isdigit():
                if len(digits) > 0:
                    rows, cols = get_ranges(inputs, i, cols)
                    if is_part_number(inputs, rows, cols, symbols):
                        part_numbers.append(int(digits))
                    digits, cols = "", []

    score = sum(part_numbers)
    return score


def calculate_part_2(inputs: list[str]) -> int:
    gears: dict[int, dict[int, list[int]]] = {}
    symbols = list(string.punctuation)
    symbols.remove(".")

    for i in range(len(inputs)):
        digits, cols = "", []

        for j in range(len(inputs[i])):
            char_at: str = inputs[i][j]

            if char_at.isdigit():
                digits += char_at
                cols.append(j)

            if j == (len(inputs[i]) - 1) or not char_at.isdigit():
                if len(digits) > 0:
                    rows, cols = get_ranges(inputs, i, cols)
                    if is_part_number(inputs, rows, cols, symbols):
                        update_gears(gears, inputs, rows, cols, int(digits))
                    digits, cols = "", []

    gear_ratios = get_gear_ratios(gears)
    score = sum(gear_ratios)
    return score


def main() -> None:
    inputs = get_input()
    print(calculate_part_1(inputs))
    print(calculate_part_2(inputs))


if __name__ == "__main__":
    main()
