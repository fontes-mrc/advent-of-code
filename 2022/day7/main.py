import pathlib


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def join_path(root: str, item: str) -> str:
    if root == "/":
        return f"/{item}"
    else:
        return f"{root}/{item}"


def create_dir(pointer: str, target: str, dirs_: dict) -> str:
    new_dir = join_path(pointer, target)

    if not new_dir in dirs_:
        dirs_[new_dir] = {
            "type": "dir",
            "items": [],
            "parent": pointer,
            "size": 0,
        }

    return new_dir


def parse_cd(dirs_: dict, pointer: str, input_: str) -> str:
    target = input_[5:]

    if target == "/":
        return "/"
    elif target == "..":
        return dirs_[pointer]["parent"]
    else:
        return create_dir(pointer, target, dirs_)


def parse_new_dir(dirs_: dict, pointer: str, input_: str) -> str:
    target = input_[4:]
    create_dir(pointer, target, dirs_)
    return pointer


def parse_new_file(dirs_: dict, pointer: str, input_: str) -> str:
    size = int(input_.split(" ")[0])
    name = join_path(pointer, input_.split(" ")[1])
    dirs_[name] = {"type": "file", "parent": pointer, "size": size}

    temp_pointer = pointer
    while temp_pointer:
        dirs_[temp_pointer]["size"] += size
        temp_pointer = dirs_[temp_pointer]["parent"]

    return pointer


def get_smallest_possible(items: list[int], n: int) -> int:
    m = len(items) // 2

    # the middle value is the smallest possible value greater than n
    if items[m] >= n and items[m - 1] < n:
        return items[m]

    # the middle values are both greater than n
    elif items[m] > n and items[m - 1] > n:
        return get_smallest_possible(items[:m], n)

    # the middle values are both smaller than n
    else:
        return get_smallest_possible(items[m:], n)


def calculate_part_1(input_: list[str]) -> int:
    dirs_ = {"/": {"type": "dir", "items": [], "parent": None, "size": 0}}

    pointer = "/"
    for row in input_:
        if row.startswith("$ ls"):
            continue
        elif row.startswith("$ cd"):
            pointer = parse_cd(dirs_, pointer, row)
        elif row.startswith("dir"):
            pointer = parse_new_dir(dirs_, pointer, row)
        else:
            pointer = parse_new_file(dirs_, pointer, row)

    selected_dirs = filter(
        lambda x: x["size"] <= 100_000 and x["type"] == "dir",
        dirs_.values(),
    )

    score = sum([d["size"] for d in selected_dirs])

    return score


def calculate_part_2(input_: list[str]) -> int:
    dirs_ = {"/": {"type": "dir", "items": [], "parent": None, "size": 0}}

    pointer = "/"
    for row in input_:
        if row.startswith("$ ls"):
            continue
        elif row.startswith("$ cd"):
            pointer = parse_cd(dirs_, pointer, row)
        elif row.startswith("dir"):
            pointer = parse_new_dir(dirs_, pointer, row)
        else:
            pointer = parse_new_file(dirs_, pointer, row)

    total_disk = 70_000_000
    needed_disk = 30_000_000
    used_disk = dirs_["/"]["size"]
    gap_disk = used_disk - (total_disk - needed_disk)

    sizes = [d["size"] for d in dirs_.values()]
    sizes.sort()

    return get_smallest_possible(sizes, gap_disk)


def main() -> None:
    input_ = get_input()
    print(calculate_part_1(input_))
    print(calculate_part_2(input_))


if __name__ == "__main__":
    main()
