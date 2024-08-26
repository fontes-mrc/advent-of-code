import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.append(ROOT.as_posix())

from common.eval import aoc_eval
from common.input import get_input

INPUT = get_input("$(YEAR)", "$(DAY)")


@aoc_eval
def resolve():
    ##################################
    # --- Put solution code here --- #
    ##################################
    pass


if __name__ == "__main__":
    print(resolve())
