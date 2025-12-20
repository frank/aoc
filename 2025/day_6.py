from pathlib import Path
from typing import Any
import numpy as np

TEST = False

OPS = {"+": np.sum, "*": np.prod}


def get_data() -> list[str]:
    day_n = Path(__file__).stem.split("_")[1]
    test_suffix = "_test" if TEST else ""
    fpath = Path(__file__).parent / "inputs" / f"day_{day_n}{test_suffix}.txt"
    with open(fpath, "r") as file:
        data = file.read().splitlines()
    return data


def process_data_part_one(data: list[str]) -> Any:
    processed = {"numbers": [], "operations": []}
    for line in data[:-1]:
        processed["numbers"].append([int(n) for n in line.strip().split()])
    processed["numbers"] = np.array(processed["numbers"]).T
    processed["operations"] = [OPS[op] for op in data[-1].split()]
    return processed


def part_one(data):
    total = 0

    for i in range(len(data["operations"])):
        total += data["operations"][i](data["numbers"][i])

    print("Part One:", total, end=" ")
    if TEST:
        print("[SUCCESS]" if total == 4277556 else "[FAILURE]")
    else:
        print()


def process_data_part_two(data: list[str]) -> Any:
    processed = {"numbers": [], "operations": []}

    numbers = []
    for line in data[:-1]:
        numbers.append([(c if c != " " else "") for c in line])
    numbers = np.array(numbers).T.tolist()
    numbers = ["".join(n) for n in numbers]

    entry = []
    for n in numbers:
        if n == "":
            processed["numbers"].append(entry)
            entry = []
            continue
        entry.append(int(n))
    processed["numbers"].append(entry)

    processed["operations"] = [OPS[op] for op in data[-1].split()]
    return processed


def part_two(data):
    total = 0

    for i in range(len(data["operations"])):
        total += data["operations"][i](data["numbers"][i])

    print("Part Two:", total, end=" ")
    if TEST:
        print("[SUCCESS]" if total == 3263827 else "[FAILURE]")
    else:
        print()


if __name__ == "__main__":
    data = get_data()
    part_one(process_data_part_one(data))
    part_two(process_data_part_two(data))
