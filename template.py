from pathlib import Path
from typing import Any

TEST = True


def get_data() -> list[str]:
    day_n = Path(__file__).stem.split("_")[1]
    test_suffix = "_test" if TEST else ""
    fpath = Path(__file__).parent / "inputs" / f"day_{day_n}{test_suffix}.txt"
    with open(fpath, "r") as file:
        data = file.read().splitlines()
    return data


def process_data(data: list[str]) -> Any:
    processed = []
    ...
    return processed


def part_one(data):
    result = 0
    ...
    print("Part One:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 1 else "[FAILURE]")
    else:
        print()


def part_two(data):
    result = 0
    ...
    print("Part Two:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 1 else "[FAILURE]")
    else:
        print()


if __name__ == "__main__":
    data = get_data()
    data = process_data(data)
    part_one(data)
    part_two(data)
