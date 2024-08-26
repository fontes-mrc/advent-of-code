from dataclasses import dataclass
from timeit import default_timer as timer
from typing import Callable

from common.vars import EVAL_RUNS


@dataclass
class Response:
    value: int
    best: float

    @property
    def best_ms(self) -> float:
        return round(self.best * 1000, 4)


def aoc_eval(func: Callable[..., int]) -> Callable[..., Response]:
    def wrapper(*args, **kwargs):
        best = float("inf")
        for _ in range(EVAL_RUNS):
            start = timer()
            value = func(*args, **kwargs)
            end = timer()
            best = min(best, end - start)
        return Response(value=value, best=best)

    return wrapper
