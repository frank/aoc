from pathlib import Path
from typing import Any
import numpy as np

TEST = False


def get_data() -> list[str]:
    day_n = Path(__file__).stem.split("_")[1]
    test_suffix = "_test" if TEST else ""
    fpath = Path(__file__).parent / "inputs" / f"day_{day_n}{test_suffix}.txt"
    with open(fpath, "r") as file:
        data = file.read().splitlines()
    return data


def process_data(data: list[str]) -> Any:
    i = 0
    processed = {"ranges": [], "ids": []}
    while data[i] != "":
        processed["ranges"].append([int(n) for n in data[i].split("-")])
        i += 1
    i += 1
    while i < len(data):
        processed["ids"].append(int(data[i]))
        i += 1
    return processed


def part_one(data):
    result = 0
    ranges = data["ranges"]
    ids = np.array(data["ids"])
    matches = []
    for r in ranges:
        starts = ids >= r[0]
        ends = ids <= r[1]
        matches.append(starts & ends)
    matches = np.array(matches)
    matches = np.max(matches, axis=0)
    result = np.sum(matches)
    print("Part One:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 3 else "[FAILURE]")
    else:
        print()


def part_two(data):
    result = 0
    ranges = data["ranges"]

    ranges = sorted(ranges, key=lambda x: x[0])
    # clean up overlapping ranges
    i = 0
    while i < len(ranges) - 1:
        if ranges[i][1] >= ranges[i + 1][0]:
            if ranges[i + 1][1] > ranges[i][1]:
                ranges[i][1] = ranges[i + 1][1]
            ranges.pop(i + 1)
            continue
        i += 1
    ranges = np.array(ranges)
    result = np.sum(ranges[:, 1] - ranges[:, 0] + 1)

    print("Part Two:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 15 else "[FAILURE]")
    else:
        print()


if __name__ == "__main__":
    data = get_data()
    data = process_data(data)
    part_one(data)
    part_two(data)
