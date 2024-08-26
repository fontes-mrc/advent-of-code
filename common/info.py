from dataclasses import dataclass


@dataclass
class DayPartInfo:
    expected: int | None = None
    result: int | None = None
    elapsed: float | None = None


@dataclass
class DayInfo:
    day: int
    year: int
    title: str
    part1: DayPartInfo
    part2: DayPartInfo

    def __post_init__(self) -> None:
        for key in ["part1", "part2"]:
            part = getattr(self, key)

            if part is None:
                part = DayPartInfo()

            if isinstance(part, (tuple, list)):
                part = DayPartInfo(*part)

            if isinstance(part, dict):
                part = DayPartInfo(**part)

            setattr(self, key, part)

    def to_dict(self) -> dict:
        return {
            "day": self.day,
            "year": self.year,
            "title": self.title,
            "part1": self.part1.__dict__,
            "part2": self.part2.__dict__,
        }
