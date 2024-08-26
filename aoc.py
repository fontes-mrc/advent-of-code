import json
from argparse import ArgumentParser
from pathlib import Path
from subprocess import run

from common.eval import Response
from common.info import DayInfo, DayPartInfo
from common.vars import FOLDER_ID_STR

ROOT = Path(__file__).parent
SOLUTIONS = ROOT / "solutions"
BOILERPLATE = (ROOT / "boilerplate" / "solution.py").read_text()


def setup(year: int, day: int) -> None:
    folder = SOLUTIONS / FOLDER_ID_STR.format(year=year, day=day)
    folder.mkdir(parents=True, exist_ok=True)
    description = folder / "description.md"
    if not description.exists():
        description.write_text(
            f"## Advent of Code {year}\n\n### Day {day}: <Day Title>\n..."
        )

    for part in ["part1", "part2"]:
        fl = folder / f"{part}.py"
        if not fl.exists():
            code = BOILERPLATE.replace('"$(YEAR)"', str(year))
            code = code.replace('"$(DAY)"', str(day))
            fl.write_text(code)

    print(f"Setup for year {year}, day {day} complete.")


def info(year: int, day: int, force: bool = False) -> None:
    def get_response(script: Path) -> Response:
        response = run(["python3", script], capture_output=True)
        return eval(response.stdout.decode().replace("\n", ""))

    folder = SOLUTIONS / FOLDER_ID_STR.format(year=year, day=day)
    part1 = folder / "part1.py"
    part2 = folder / "part2.py"
    description = folder / "description.md"
    info = folder / "info.json"

    title = description.read_text().split("\n")[2].replace("### ", "").split(": ")[1]
    part1_response = get_response(part1)
    part2_response = get_response(part2)

    day_info = None
    if info.exists():
        raw = info.read_text()

        if len(raw) > 0:
            data = json.loads(raw)
            day_info = DayInfo(**data)

            if force:
                day_info.part1.result = part1_response.value
                day_info.part1.elapsed = part1_response.best_ms

                day_info.part2.result = part2_response.value
                day_info.part2.elapsed = part2_response.best_ms

    if not day_info:
        day_info = DayInfo(
            year=year,
            day=day,
            title=title,
            part1=DayPartInfo(
                result=part1_response.value,
                elapsed=part1_response.best_ms,
            ),
            part2=DayPartInfo(
                result=part2_response.value,
                elapsed=part2_response.best_ms,
            ),
        )

    info.write_text(json.dumps(day_info.to_dict(), indent=4))
    print(json.dumps(day_info.to_dict(), indent=4))


def readme() -> None:
    def get_infos() -> dict[int, list[DayInfo]]:
        info_files_pattern = FOLDER_ID_STR.format(year=0, day=0) + "/info.json"
        info_files_pattern = "**/" + info_files_pattern.replace("0", "*").replace(
            "**", "*"
        )
        info_files = sorted(SOLUTIONS.glob(info_files_pattern))

        infos = []
        for info_file in info_files:
            raw = info_file.read_text()
            data = json.loads(raw)
            infos.append(DayInfo(**data))

        year_infos = {}
        for info in infos:
            if info.year not in year_infos:
                year_infos[info.year] = []
            year_infos[info.year].append(info)

        return year_infos

    def tabulate_info(day_info: DayInfo) -> list[str]:
        row = []

        part1_ok = day_info.part1.result == day_info.part1.expected
        part2_ok = day_info.part2.result == day_info.part2.expected

        row.append(f"Day {day_info.day}: {day_info.title}")
        row.append("✓" if part1_ok else "✗")
        row.append(f"{day_info.part1.elapsed:.4f} ms")
        row.append("✓" if part2_ok else "✗")
        row.append(f"{day_info.part2.elapsed:.4f} ms")

        return row

    def tabulate_missing(last_day: int, ttl_days: int) -> list[str]:
        rows = []

        for day in range(last_day + 1, ttl_days + 1):
            row = [f"Day {day}"]
            row.extend([""] * 4)
            rows.append(row)

        return rows

    def serialize_table(year: int, table: list[list[str]]) -> str:
        title = f"## Progress {year}"

        col_len = [max(len(row[i]) for row in table) for i in range(len(table[0]))]
        header = " | ".join([f"{col:<{col_len[i]}}" for i, col in enumerate(table[0])])

        aligns = ["l", "c", "r", "c", "r"]
        separators = []
        for i in range(len(col_len)):
            left_sep = ":" if aligns[i] in ["l", "c"] else "-"
            right_sep = ":" if aligns[i] in ["r", "c"] else "-"

            hifen = "-"
            separators.append(f"{left_sep}{hifen * (col_len[i] - 2)}{right_sep}")

        separator = " | ".join(separators)

        body = [header, separator]
        for row in table[1:]:
            body.append(
                " | ".join([f"{col:<{col_len[i]}}" for i, col in enumerate(row)])
            )

        return f"{title}\n\n" + "\n".join(f"| {row} |" for row in body)

    readme = ROOT / "README.md"
    readme_header = ROOT / "boilerplate" / "readme_header"

    body = [readme_header.read_text()]
    infos = get_infos()

    for year, year_infos in infos.items():
        table = [["Day", "Part 1", "Time 1", "Part 2", "Time 2"]]
        table.extend([tabulate_info(info) for info in year_infos])
        table.extend(tabulate_missing(len(year_infos), 25))
        body.append(serialize_table(year, table))

    readme.write_text("\n".join(body))
    print("README.md updated.")


def main() -> None:
    parser = ArgumentParser()

    year_args = {
        "type": int,
        "choices": [2023],
        "required": True,
    }

    day_args = {
        "type": int,
        "choices": range(1, 26),
        "required": True,
    }

    subparsers = parser.add_subparsers(dest="command")

    setup_parser = subparsers.add_parser("setup")
    setup_parser.add_argument(
        "--year",
        "-y",
        **year_args,
    )
    setup_parser.add_argument(
        "--day",
        "-d",
        **day_args,
    )

    info_parser = subparsers.add_parser("info")
    info_parser.add_argument(
        "--year",
        "-y",
        **year_args,
    )
    info_parser.add_argument(
        "--day",
        "-d",
        **day_args,
    )
    info_parser.add_argument(
        "--force",
        action="store_true",
    )

    subparsers.add_parser("readme")

    args = parser.parse_args()

    if args.command == "setup":
        setup(args.year, args.day)

    elif args.command == "info":
        info(args.year, args.day, args.force)

    elif args.command == "readme":
        readme()


if __name__ == "__main__":
    main()
