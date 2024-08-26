from common.vars import FOLDER_ID_STR, SOLUTIONS


def get_input(year: int, day: int) -> str:
    input_path = SOLUTIONS / FOLDER_ID_STR.format(year=year, day=day) / "input.txt"
    data = input_path.read_text()

    if data.endswith("\n"):
        data = data[:-1]

    return data
