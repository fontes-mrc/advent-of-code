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


def create_dir(pointer: str, target: str, dirs: dict) -> str:
    new_dir = join_path(pointer, target)

    if not new_dir in dirs:
        dirs[new_dir] = {
            "type": "dir",
            "items": [],
            "parent": pointer,
            "size": 0,
        }

    return new_dir


def parse_cd(dirs: dict, pointer: str, input: str) -> str:
    target = input[5:]

    if target == "/":
        return "/"
    elif target == "..":
        return dirs[pointer]["parent"]
    else:
        return create_dir(pointer, target, dirs)


def parse_new_dir(dirs: dict, pointer: str, input: str) -> str:
    target = input[4:]
    create_dir(pointer, target, dirs)
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


def parse_new_file(dirs: dict, pointer: str, input: str) -> str:
    size = int(input.split(" ")[0])
    name = join_path(pointer, input.split(" ")[1])
    dirs[name] = {"type": "file", "parent": pointer, "size": size}

    temp_pointer = pointer
    while temp_pointer:
        dirs[temp_pointer]["size"] += size
        temp_pointer = dirs[temp_pointer]["parent"]

    return pointer


def calculate_part_1(inputs: list[str]) -> int:
    dirs = {"/": {"type": "dir", "items": [], "parent": None, "size": 0}}

    pointer = "/"
    for input in inputs:
        if input.startswith("$ ls"):
            continue
        elif input.startswith("$ cd"):
            pointer = parse_cd(dirs, pointer, input)
        elif input.startswith("dir"):
            pointer = parse_new_dir(dirs, pointer, input)
        else:
            pointer = parse_new_file(dirs, pointer, input)

    selected_dirs = filter(
        lambda x: x["size"] <= 100_000 and x["type"] == "dir",
        dirs.values(),
    )

    score = sum([d["size"] for d in selected_dirs])

    return score


def calculate_part_2(inputs: list[str]) -> int:
    dirs = {"/": {"type": "dir", "items": [], "parent": None, "size": 0}}

    pointer = "/"
    for input in inputs:
        if input.startswith("$ ls"):
            continue
        elif input.startswith("$ cd"):
            pointer = parse_cd(dirs, pointer, input)
        elif input.startswith("dir"):
            pointer = parse_new_dir(dirs, pointer, input)
        else:
            pointer = parse_new_file(dirs, pointer, input)

    total_disk = 70_000_000
    needed_disk = 30_000_000
    used_disk = dirs["/"]["size"]
    gap_disk = used_disk - (total_disk - needed_disk)

    sizes = [d["size"] for d in dirs.values()]
    sizes.sort()

    return get_smallest_possible(sizes, gap_disk)


def main() -> None:
    inputs = get_input()
    print(calculate_part_1(inputs))
    print(calculate_part_2(inputs))


if __name__ == "__main__":
    main()
