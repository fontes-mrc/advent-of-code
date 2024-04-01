from argparse import ArgumentParser
from dataclasses import dataclass, field
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.padding import Padding
from rich.table import Table, box
from rich_argparse import RichHelpFormatter
from enum import StrEnum
import json
from subprocess import run
from timeit import timeit


ROOT = Path(__file__).parent / "aoc"
CONSOLE = Console()
MAX_DAYS = 25

RichHelpFormatter.styles["argparse.args"] = "green"
RichHelpFormatter.styles["argparse.groups"] = "magenta"
RichHelpFormatter.styles["argparse.metavar"] = "gray50 italic"


class Language(StrEnum):
    PYTHON = "python"

TIME_COLORS = {
    0.02: "cyan",
    0.2: "green",
    0.4: "yellow",
    0.8: "orange",
    1.6: "red",
}

EXTENSION = {
    Language.PYTHON: "py",
}

EXECUTABLE = {
    Language.PYTHON: "python",
}


@dataclass
class Solution:
    code1: Path
    code2: Path
    result1: str | None
    result2: str | None
    time_complexity: str
    space_complexity: str
    best_time: float
    best_time_label: str


@dataclass
class Day:
    path: Path
    title: str = field(init=False)
    description: str = field(init=False)
    expected1: str = field(init=False)
    expected2: str = field(init=False)
    solutions: dict[str, Solution] = field(init=False, default_factory=dict)

    def __post_init__(self) -> None:
        self.refresh()

    def refresh(self) -> None:
        info = json.loads((self.path / "info.json").read_text())
        description = (self.path / "description.md").read_text()
        title = info["title"]
        expected1 = info["expected"]["part1"]
        expected2 = info["expected"]["part2"]

        description = description.replace("$(part1)", expected1)
        description = description.replace("$(part2)", expected2)

        solutions: dict[str, Solution] = {}

        for sol in info.get("solutions", []):
            lang = Language(sol["lang"])
            code1 = self.path / "solution" / lang.value / f"part1.{EXTENSION[lang]}"
            code2 = self.path / "solution" / lang.value / f"part2.{EXTENSION[lang]}"
            result1 = sol.get("results", {}).get("part1")
            result2 = sol.get("results", {}).get("part2")
            complexities = sol.get("complexity", {})
            time_complexity = complexities.get("time", "unknown")
            space_complexity = complexities.get("space", "unknown")
            best_time = min([float(t) for t in sol["times"]] or [0])
            best_time_label = ""
            for t, color in TIME_COLORS.items():
                if best_time <= t:
                    best_time_label = f"[{color}]{best_time:.6f} s[/{color}]"
                    break

            solutions[lang] = Solution(
                code1=code1,
                code2=code2,
                result1=result1,
                result2=result2,
                time_complexity=time_complexity,
                space_complexity=space_complexity,
                best_time=best_time,
                best_time_label=best_time_label,
            )

        self.title = title
        self.description = description
        self.expected1 = expected1
        self.expected2 = expected2
        self.solutions = solutions


@dataclass
class Year:
    days: dict[int, Day]


class AoE:
    def __init__(self) -> None:
        self.years = self._parse_years()

    @staticmethod
    def _parse_years() -> dict[int, Year]:
        years = {}
        for year in ROOT.iterdir():
            if year.is_dir():
                days = {}
                for day in year.iterdir():
                    if day.is_dir():
                        days[int(day.name[3:])] = Day(day)
                years[int(year.name)] = Year(days)
        return years

    def print_solution(self, year: int, day: int, lang: Language) -> None:
        day_props: Day = self.years[year].days[day]
        solution = day_props.solutions[lang]

        CONSOLE.print(f"[green bold]Advent of Code {year} - Day {day}[/green bold]")
        CONSOLE.print(f"[green]Description[/green]:")
        CONSOLE.print(
            Padding(
                Markdown(day_props.description),
                (1, 4),
            )
        )

        for part, code in [("Part 1", solution.code1), ("Part 2", solution.code2)]:
            CONSOLE.print(f"[green]Solution for {part} in {lang}:[/green]")
            CONSOLE.print(
                Padding(
                    Syntax(
                        code.read_text(),
                        EXTENSION[lang],
                        line_numbers=True,
                        word_wrap=True,
                        indent_guides=True,
                        tab_size=2,
                        padding=1,
                    ),
                    (1, 4),
                )
            )

    def print_progress(self, year: int, lang: Language) -> None:
        columns = {
            "Day": "left",
            "Part 1": "center",
            "Part 2": "center",
            "Best Time": "right",
            "Time Comp.": "left",
            "Space Comp.": "left",
        }

        table = Table(
            title=f"[green]Advent of Code {year} Progress[/green]",
            show_lines=False,
            box=box.MARKDOWN,
        )
        for col, align in columns.items():
            table.add_column(col, justify=align)  # type: ignore

        success = "[green]✓[/green]"
        fail = "[red]✕[/red]"

        for day in range(1, MAX_DAYS + 1):
            day_props = self.years[year].days.get(day)
            if day_props:
                solution = day_props.solutions.get(lang)
                if solution:
                    table.add_row(
                        f"[bold]Day {day}[/bold]: [italic]{day_props.title}[/italic]",
                        (
                            success
                            if solution.result1 == day_props.expected1
                            else fail
                            if solution.result1
                            else ""
                        ),
                        (
                            success
                            if solution.result2 == day_props.expected2
                            else fail
                            if solution.result2
                            else ""
                        ),
                        solution.best_time_label,
                        solution.time_complexity,
                        solution.space_complexity,
                    )
            else:
                table.add_row(f"[bold]Day {day}[/bold]", "", "", "", "", "")

        CONSOLE.print(table)

    def run_perftest(self, year: int, lang: Language, day: int | None = None) -> None:
        days = range(1, MAX_DAYS + 1) if day is None else [day]
        for day in days:
            day_props = self.years[year].days.get(day)
            if day_props:
                solution = day_props.solutions.get(lang)
                if solution:
                    result1: str | None = None
                    result2: str | None = None
                    times = []

                    if solution.code1.exists():
                        result1 = run(
                            [EXECUTABLE[lang], solution.code1],
                            capture_output=True,
                            text=True,
                        ).stdout.replace("\n", "")

                    if solution.code2.exists():
                        result2 = run(
                            [EXECUTABLE[lang], solution.code2],
                            capture_output=True,
                            text=True,
                        ).stdout.replace("\n", "")

                        for _ in range(10):
                            time = timeit(
                                lambda: run(
                                    [EXECUTABLE[lang], solution.code2],  # type: ignore
                                    capture_output=True,
                                    text=True,
                                ),
                                number=1,
                            )

                            times.append(time)

                    info = json.loads((day_props.path / "info.json").read_text())
                    lang_info = next(
                        (sol for sol in info["solutions"] if sol["lang"] == lang.value),
                        None,
                    )
                    lang_info["results"] = {"part1": result1, "part2": result2}  # type: ignore
                    lang_info["times"] = times  # type: ignore

                    (day_props.path / "info.json").write_text(
                        json.dumps(info, indent=4)
                    )

                day_props.refresh()


def main():
    parser = ArgumentParser(
        description="Advent of Code CLI", formatter_class=RichHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    solution_parser = subparsers.add_parser(
        "solution", help="Print solution", formatter_class=RichHelpFormatter
    )
    solution_parser.add_argument(
        "-y", "--year", type=int, help="Year", choices=[2023], required=True
    )
    solution_parser.add_argument(
        "-d",
        "--day",
        type=int,
        help="Day",
        choices=range(1, MAX_DAYS + 1),
        required=True,
    )
    solution_parser.add_argument(
        "-l",
        "--lang",
        help="Language",
        choices=[lang.value for lang in Language],
        required=True,
    )

    progress_parser = subparsers.add_parser(
        "progress", help="Print progress", formatter_class=RichHelpFormatter
    )
    progress_parser.add_argument(
        "-y", "--year", type=int, help="Year", choices=[2023], required=True
    )
    progress_parser.add_argument(
        "-l",
        "--lang",
        help="Language",
        choices=[lang.value for lang in Language],
        required=True,
    )

    perftest_parser = subparsers.add_parser(
        "perftest", help="Run performance test", formatter_class=RichHelpFormatter
    )
    perftest_parser.add_argument(
        "-y", "--year", type=int, help="Year", choices=[2023], required=True
    )
    perftest_parser.add_argument(
        "-l",
        "--lang",
        help="Language",
        choices=[lang.value for lang in Language],
        required=True,
    )
    perftest_parser.add_argument(
        "-d",
        "--day",
        type=int,
        help="Day",
        choices=range(1, MAX_DAYS + 1),
        required=False,
    )

    args = parser.parse_args()

    aoe = AoE()

    if args.command == "solution":
        aoe.print_solution(args.year, args.day, Language(args.lang))
    elif args.command == "progress":
        aoe.print_progress(args.year, Language(args.lang))
    elif args.command == "perftest":
        aoe.run_perftest(args.year, Language(args.lang), args.day)
        aoe.print_progress(args.year, Language(args.lang))


if __name__ == "__main__":
    main()
