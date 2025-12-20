from pathlib import Path
from typing import Any
from functools import cache

TEST = False


def get_data() -> list[str]:
    day_n = Path(__file__).stem.split("_")[1]
    test_suffix = "_test" if TEST else ""
    fpath = Path(__file__).parent / "inputs" / f"day_{day_n}{test_suffix}.txt"
    with open(fpath, "r") as file:
        data = file.read().splitlines()
    return data


def process_data(data: list[str]) -> Any:
    processed = []
    for r in data[0].strip().split(","):
        start, end = map(int, r.split("-"))
        processed.append((start, end))
    return processed


def part_one(data):
    total = 0
    for start, end in data:
        for n in range(start, end + 1):  # making the range inclusive
            n_str = str(n)
            if len(n_str) % 2 == 1:
                continue
            if n_str[: len(n_str) // 2] == n_str[len(n_str) // 2 :]:
                total += n
    print("Part One:", total, end=" ")
    if TEST:
        print("[SUCCESS]" if total == 1227775554 else "[FAILURE]")
    else:
        print()


@cache
def get_divisors_minus_self(n: int) -> list[int]:
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def part_two(data):
    total = 0
    for start, end in data:
        for n in range(start, end + 1):  # making the range inclusive
            match = False
            n_str = str(n)
            # e.g. for a digit with 10 digits iterate over [5, 2, 1]
            for divisor in reversed(get_divisors_minus_self(len(n_str))):
                # check repetitions of all groups of size "divisor". if all are equal it's a match
                if match:
                    break
                match = True
                for i in range((len(n_str) // divisor) - 1):
                    if (
                        n_str[i * divisor : (i + 1) * divisor]
                        != n_str[(i + 1) * divisor : (i + 2) * divisor]
                    ):
                        match = False
                        break

            if match:
                total += n

    print("Part Two:", total, end=" ")
    if TEST:
        print("[SUCCESS]" if total == 4174379265 else "[FAILURE]")
    else:
        print()


if __name__ == "__main__":
    data = get_data()
    data = process_data(data)
    part_one(data)
    part_two(data)
