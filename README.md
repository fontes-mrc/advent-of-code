# Advent of Code

In this repository, you'll find my responses to the challenges proposed in Advent of Code. The main goal is to practice problem-solving and share the results with the community, so others can benefit from some of my ideas.

## CLI Tool

I've created a CLI tool to help me manage the project. It's a simple Python script that allows me to run the tests and get the status of each day.

Run the following command to see the available options:

```bash
$ python3 aoc.py --help
```

## Updating Progress

The best times and results are calculated in a controlled environment using a docker container with resources limited to 1 CPU, 512MB of RAM and the CLI tool:

```bash
$ docker run --rm -it -v $(pwd):/app -w /app --cpus 1 --memory 512m python:3.12 bash
$ pip install -r requirements.txt
$ python3 aoc.py perftest -y 2023 -l python
```

## Progress 2023

### Python

| Day                                    | Part 1 | Part 2 |  Best Time | Time Comp. | Space Comp.   |
|----------------------------------------|--------|--------|------------|------------|---------------|
| Day 1: Trebuchet?!                     |   ✓    |   ✓    | 0.018646 s | O(nm)      | O(n)          |
| Day 2: Cube Conundrum                  |   ✓    |   ✓    | 0.017580 s | O(nmk)     | O(1)          |
| Day 3: Gear Ratios                     |   ✓    |   ✓    | 0.021548 s | O(nmk)     | O(nm)         |
| Day 4: Scratchcards                    |   ✓    |   ✓    | 0.019948 s | O(nm)      | O(n)          |
| Day 5: If You Give A Seed A Fertilizer |   ✓    |   ✓    | 0.031844 s | O(nm)      | O(n)          |
| Day 6: Wait For It                     |   ✓    |   ✓    | 0.017258 s | O(1)       | O(1)          |
| Day 7: Camel Cards                     |   ✓    |   ✓    | 0.022017 s | O(n log n) | O(n)          |
| Day 8: Haunted Wasteland               |   ✓    |   ✓    | 0.040780 s | O(nk)      | O(nm + n + k) |
| Day 9: Mirage Maintenance              |   ✓    |   ✓    | 0.018498 s | O(nm)      | O(n)          |
| Day 10                                 |        |        |            |            |               |
| Day 11                                 |        |        |            |            |               |
| Day 12                                 |        |        |            |            |               |
| Day 13                                 |        |        |            |            |               |
| Day 14                                 |        |        |            |            |               |
| Day 15                                 |        |        |            |            |               |
| Day 16                                 |        |        |            |            |               |
| Day 17                                 |        |        |            |            |               |
| Day 18                                 |        |        |            |            |               |
| Day 19                                 |        |        |            |            |               |
| Day 20                                 |        |        |            |            |               |
| Day 21                                 |        |        |            |            |               |
| Day 22                                 |        |        |            |            |               |
| Day 23                                 |        |        |            |            |               |
| Day 24                                 |        |        |            |            |               |
| Day 25                                 |        |        |            |            |               |