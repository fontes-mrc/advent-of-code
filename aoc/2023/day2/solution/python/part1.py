import re
from pathlib import Path

input_path = Path(__file__).parent.parent.parent / "input.txt"
input_ = input_path.read_text()


def parse_game(game: str) -> tuple[int, dict[str, int]]:
    game_id = int(re.findall(r"(?<=Game )\d+", game)[0])
    colors: dict[str, int] = {}
    for i in re.findall(r"\d+(?> blue| red| green)", game):
        n, color = i.split(" ")
        colors[color] = max(int(n), colors.get(color, 0))

    return game_id, colors


def resolve(input_: str) -> int:
    limits = {"red": 12, "green": 13, "blue": 14}
    return sum(
        game_id
        for game_id, colors in map(parse_game, input_.splitlines())
        if all(colors[k] <= limits[k] for k in colors.keys())
    )


print(resolve(input_))
