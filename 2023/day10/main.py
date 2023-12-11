"""
================================================================================
Advent of Code 2023
--- Day 10: Pipe Maze ---
You use the hang glider to ride the hot air from Desert Island all the way up to
the floating metal island. This island is surprisingly cold and there definitely
aren't any thermals to glide on, so you leave your hang glider behind.

You wander around for a while, but you don't find any people or animals.
However, you do occasionally find signposts labeled "Hot Springs" pointing in a
seemingly consistent direction; maybe you can find someone at the hot springs
and ask them where the desert-machine parts are made.

The landscape here is alien; even the flowers and trees are made of metal. As
you stop to admire some metal grass, you notice something metallic scurry away
in your peripheral vision and jump into a big pipe! It didn't look like any
animal you've ever seen; if you want a better look, you'll need to get ahead of
it.

Scanning the area, you discover that the entire field you're standing on is
densely packed with pipes; it was hard to tell at first because they're the same
metallic silver color as the "ground". You make a quick sketch of all of the
surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of tiles:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your
sketch doesn't show what shape the pipe has.
Based on the acoustics of the animal's scurrying, you're confident the pipe that
contains the animal is one large, continuous loop.

For example, here is a square loop of pipe:

.....
.F-7.
.|.|.
.L-J.
.....
If the animal had entered this loop in the northwest corner, the sketch would
instead look like this:

.....
.S-7.
.|.|.
.L-J.
.....
In the above diagram, the S tile is still a 90-degree F bend: you can tell
because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that aren't connected to the loop! This
sketch shows the same loop as above:

-L|F7
7S-7|
L|7||
-L-J|
L|-JF
In the above diagram, you can still figure out which pipes form the main loop:
they're the ones connected to S, pipes those pipes connect to, pipes those pipes
connect to, and so on. Every pipe in the main loop connects to its two neighbors
(including S, which will have exactly two pipes connecting to it, and which is
assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here's the same example sketch with the extra, non-main-loop pipe tiles also
shown:

7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
If you want to get out ahead of the animal, you should find the tile in the loop
that is farthest from the starting position. Because the animal is in the pipe,
it doesn't make sense to measure this by direct distance. Instead, you need to
find the tile that would take the longest number of steps along the loop to
reach from the starting point - regardless of which way around the loop the
animal went.

In the first example with the square loop:

.....
.S-7.
.|.|.
.L-J.
.....
You can count the distance each tile in the loop is from the starting point like
this:

.....
.012.
.1.3.
.234.
.....
In this example, the farthest point from the start is 4 steps away.

Here's the more complex loop again:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here are the distances for each tile on that loop:

..45.
.236.
01.78
14567
23...
Find the single giant loop starting at S. How many steps along the loop does it
take to get from the starting position to the point farthest from the starting
position?

Your puzzle answer was 6682.

--- Part Two ---
You quickly reach the farthest point of the loop, but the animal never emerges.
Maybe its nest is within the area enclosed by the loop?

To determine whether it's even worth taking the time to search for such a nest,
you should calculate how many tiles are contained within the loop. For example:

...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
The above loop encloses merely four tiles - the two pairs of . in the southwest
and southeast (marked I below). The middle . tiles (marked O below) are not in
the loop. Here is the same loop again with those regions marked:

...........
.S-------7.
.|F-----7|.
.||OOOOO||.
.||OOOOO||.
.|L-7OF-J|.
.|II|O|II|.
.L--JOL--J.
.....O.....
In fact, there doesn't even need to be a full tile path to the outside for tiles
to count as outside the loop - squeezing between pipes is also allowed! Here, I
is still within the loop and O is still outside the loop:

..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........
In both of the above examples, 4 tiles are enclosed by the loop.

Here's a larger example:

.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
The above sketch has many random bits of ground, some of which are in the loop
(I) and some of which are outside it (O):

OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO
In this larger example, 8 tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the
loop. Here's another example with many bits of junk pipe lying around that
aren't connected to the main loop at all:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
Here are just the tiles that are enclosed by the loop marked with I:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
In this last example, 10 tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the area
within the loop. How many tiles are enclosed by the loop?

Your puzzle answer was 353.
================================================================================
"""

import pathlib


def get_input() -> list[str]:
    dir_ = pathlib.Path(__file__).parent.absolute()
    with open(dir_ / "input.txt") as f:
        rows = f.readlines()
    return [r.replace("\n", "") for r in rows]


def parse_pipe(
    coords: tuple[int, int],
    pipe: str,
) -> dict[str, tuple[tuple[int, int], str]]:
    sumc = lambda x, y: tuple(map(sum, zip(x, y)))

    pipes = {
        "|": ("N", "S"),
        "-": ("E", "W"),
        "L": ("N", "E"),
        "J": ("N", "W"),
        "7": ("S", "W"),
        "F": ("S", "E"),
    }

    dirs = {
        "N": ((0, -1), "S"),
        "S": ((0, 1), "N"),
        "W": ((-1, 0), "E"),
        "E": ((1, 0), "W"),
        "M": ((0, 0), "M"),
    }

    if pipe in pipes:
        d1, d2 = pipes[pipe]
        return {
            d1: (sumc(coords, dirs[d2][0]), dirs[d2][1]),
            d2: (sumc(coords, dirs[d1][0]), dirs[d1][1]),
        }

    else:
        return {}


def parse_s(
    coord: tuple[int, int], map_: list[str]
) -> tuple[str, tuple[tuple[int, int], str]]:
    e_coord = (coord[0] + 1, coord[1])
    w_coord = (coord[0] - 1, coord[1])
    s_coord = (coord[0], coord[1] + 1)
    n_coord = (coord[0], coord[1] - 1)

    sides = []
    first_move = ((0, 0), "M")

    if map_[e_coord[1]][e_coord[0]] in ["-", "J", "7"]:
        sides.append("E")
        first_move = (e_coord, "W")

    if map_[w_coord[1]][w_coord[0]] in ["-", "L", "F"]:
        sides.append("W")
        first_move = (w_coord, "E")

    if map_[s_coord[1]][s_coord[0]] in ["|", "J", "L"]:
        sides.append("S")
        first_move = (s_coord, "N")

    if map_[n_coord[1]][n_coord[0]] in ["|", "F", "7"]:
        sides.append("N")
        first_move = (n_coord, "S")

    if "N" in sides and "S" in sides:
        return "|", first_move

    if "E" in sides and "W" in sides:
        return "-", first_move

    if "N" in sides and "E" in sides:
        return "L", first_move

    if "N" in sides and "W" in sides:
        return "J", first_move

    if "S" in sides and "W" in sides:
        return "7", first_move

    if "S" in sides and "E" in sides:
        return "F", first_move


def count_filled(points: list[tuple[int, int]], map_: list[str], new_s: str) -> int:
    clean_map = [
        ["." if (j, i) not in points else map_[i][j] for j in range(len(map_[i]))]
        for i in range(len(map_))
    ]

    clean_map[points[0][1]][points[0][0]] = new_s

    filled = 0
    for row in clean_map:
        for i, char in enumerate(row):
            if char != ".":
                continue

            intersect = 0
            corner_pipes = []
            for j in range(i + 1, len(row)):
                if row[j] in "|":
                    intersect += 1
                if row[j] in "FL":
                    corner_pipes.append(row[j])
                if (
                    len(corner_pipes) != 0
                    and row[j] == "J"
                    and corner_pipes[-1] == "F"
                    or row[j] == "7"
                    and corner_pipes[-1] == "L"
                ):
                    corner_pipes.pop(-1)
                    intersect += 1

            if intersect % 2 == 1:
                filled += 1

    return filled


def part1(input_: list[str]) -> int:
    pipes, s = {}, ()
    for i in range(len(input_)):
        for j in range(len(input_[i])):
            coord = (j, i)
            pipe = input_[i][j]

            pipes.update({coord: parse_pipe(coord, pipe)})
            if pipe == "S":
                s = coord

    path = [s]
    _, move = parse_s(s, input_)
    while move:
        path.append(move[0])
        move = pipes[move[0]].get(move[1], None)

    return len(path) // 2


def part2(input_: list[str]) -> int:
    pipes, s = {}, ()
    for i in range(len(input_)):
        for j in range(len(input_[i])):
            coord = (j, i)
            pipe = input_[i][j]

            pipes.update({coord: parse_pipe(coord, pipe)})
            if pipe == "S":
                s = coord

    path = [s]
    new_s, move = parse_s(s, input_)
    while move:
        path.append(move[0])
        move = pipes[move[0]].get(move[1], None)

    return count_filled(path, input_, new_s)


def main() -> None:
    input_ = get_input()
    print(part1(input_))
    print(part2(input_))


if __name__ == "__main__":
    main()
