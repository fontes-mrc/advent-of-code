"""
================================================================================
Advent of Code 2023
--- Day 11: Cosmic Expansion ---
You continue following signs for "Hot Springs" and eventually come across an
observatory. The Elf within turns out to be a researcher studying cosmic
expansion using the giant telescope here.

He doesn't know anything about the missing machine parts; he's only visiting for
this research project. However, he confirms that the hot springs are the
next-closest area likely to have people; he'll even take you straight there once
he's done with today's observation analysis.

Maybe you can help him with the analysis to speed things up?

The researcher has collected a bunch of data and compiled the data into a single
giant image (your puzzle input). The image includes empty space (.) and galaxies
(#). For example:

...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
The researcher is trying to figure out the sum of the lengths of the shortest
path between every pair of galaxies. However, there's a catch: the universe
expanded in the time it took the light from those galaxies to reach the
observatory.

Due to something involving gravitational effects, only some space expands. In
fact, the result is that any rows or columns that contain no galaxies should
all actually be twice as big.

In the above example, three columns and two rows contain no galaxies:

   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^
These rows and columns need to be twice as big; the result of cosmic expansion
therefore looks like this:

....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......
Equipped with this expanded universe, the shortest path between every pair of
galaxies can be found. It can help to assign every galaxy a unique number:

....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......
In these 9 galaxies, there are 36 pairs. Only count each pair once; order within
the pair doesn't matter. For each pair, find any shortest path between the two
galaxies using only steps that move up, down, left, or right exactly one . or #
at a time. (The shortest path between two galaxies is allowed to pass through
another galaxy.)

For example, here is one of the shortest paths between galaxies 5 and 9:

....1........
.........2...
3............
.............
.............
........4....
.5...........
.##.........6
..##.........
...##........
....##...7...
8....9.......
This path has length 9 because it takes a minimum of nine steps to get from
galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9
itself). Here are some other example shortest path lengths:

Between galaxy 1 and galaxy 7: 15
Between galaxy 3 and galaxy 6: 17
Between galaxy 8 and galaxy 9: 5
In this example, after expanding the universe, the sum of the shortest path
between all 36 pairs of galaxies is 374.

Expand the universe, then find the length of the shortest path between every
pair of galaxies. What is the sum of these lengths?

Your puzzle answer was 9509330.

--- Part Two ---
The galaxies are much older (and thus much farther apart) than the researcher
initially estimated.

Now, instead of the expansion you did before, make each empty row or column one
million times larger. That is, each empty row should be replaced with 1000000
empty rows, and each empty column should be replaced with 1000000 empty columns.

(In the example above, if each empty row or column were merely 10 times larger,
the sum of the shortest paths between every pair of galaxies would be 1030. If
each empty row or column were merely 100 times larger, the sum of the shortest
paths between every pair of galaxies would be 8410. However, your universe will
need to expand far beyond these values.)

Starting with the same initial image, expand the universe according to these new
rules, then find the length of the shortest path between every pair of galaxies.
What is the sum of these lengths?

Your puzzle answer was 635832237682.
================================================================================
"""

import pathlib
from itertools import combinations


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def empty_spaces(input_: list[str]) -> dict[str, list[int]]:
    spaces = {"x": [], "y": []}

    for i, row in enumerate(input_):
        if len(set(row)) == 1:
            spaces["y"].append(i)

    for i in range(len(input_[0])):
        if len(set([r[i] for r in input_])) == 1:
            spaces["x"].append(i)

    return spaces


def offset(
    spaces: dict[str, list[int]],
    x: int,
    y: int,
    n: int = 1,
) -> tuple[int, int]:
    x_offset = sum(i < x for i in spaces["x"]) * n
    y_offset = sum(i < y for i in spaces["y"]) * n

    return (x + x_offset, y + y_offset)


def dist(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p2[1] - p1[1]) + abs(p2[0] - p1[0])


def part1(input_: list[str]) -> int:
    spaces = empty_spaces(input_)
    points = []

    for y, row in enumerate(input_):
        for x, char in enumerate(row):
            if char == "#":
                points.append(offset(spaces, x, y))

    dists = [dist(p1, p2) for p1, p2 in combinations(points, 2)]
    return sum(dists)


def part2(input_: list[str]) -> int:
    spaces = empty_spaces(input_)
    points = []

    for y, row in enumerate(input_):
        for x, char in enumerate(row):
            if char == "#":
                points.append(offset(spaces, x, y, 1_000_000 - 1))

    dists = [dist(p1, p2) for p1, p2 in combinations(points, 2)]
    return sum(dists)


def main() -> None:
    input_ = get_input()
    print(part1(input_))
    print(part2(input_))


if __name__ == "__main__":
    main()
