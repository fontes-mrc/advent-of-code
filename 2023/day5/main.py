import pathlib


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def is_between(range: list[int], n: int) -> bool:
    start = range[0]
    end = range[1]
    return start <= n < end


def get_maps(input_: list[str]) -> dict[int, dict[tuple[int, int], int]]:
    maps: dict[int, dict[tuple[int, int], int]] = {}
    map_: dict[tuple[int, int], int] = {}

    i = 0
    for row in input_[3:]:
        if row == "":
            continue

        elif row.endswith(":"):
            maps[i] = map_
            map_ = {}
            i += 1

        else:
            dest, source, size = tuple([int(n) for n in row.split(" ")])
            map_[(source, source + size)] = dest - source

    maps[i] = map_
    return maps


def calculate_part_1(input_: list[str]) -> int:
    seeds = [int(n) for n in input_[0].split(":")[1].strip().split()]
    targets: list[int] = []
    maps = get_maps(input_)

    for seed in seeds:
        target = seed
        for map_ in maps.values():
            for range in map_.keys():
                if is_between(range, target):
                    target += map_[range]
                    break
        targets.append(target)

    return min(targets)


def calculate_part_2(input_: list[str]) -> int:
    seed_pairs = input_[0].split(":")[1].strip().split()
    seeds = [
        [int(start), int(start) + int(size)]
        for start, size in zip(seed_pairs[0::2], seed_pairs[1::2])
    ]
    seeds = [(x, 0) for x in seeds]
    targets: list[int] = []
    maps = get_maps(input_)

    while seeds:
        seed_range, map_idx = seeds.pop(0)

        if map_idx == max(maps.keys()):
            targets.append(seed_range[0])
            continue

        for range in maps[map_idx]:
            left = is_between(range, seed_range[0])
            right = is_between(range, seed_range[1] - 1)

            if not left and not right:
                continue

            if left and right:
                offset = maps[map_idx][range]
                seed_range = [n + offset for n in seed_range]
                seeds.append((seed_range, map_idx + 1))
                break

            if left:
                split = range[1]
            if right:
                split = range[0]

            seeds.append(((seed_range[0], split), map_idx))
            seeds.append(((split, seed_range[1]), map_idx))
            break

        else:
            seeds.append((seed_range, map_idx + 1))

    return min(targets)


def main() -> None:
    input_ = get_input()
    print(calculate_part_1(input_))
    print(calculate_part_2(input_))


if __name__ == "__main__":
    main()
