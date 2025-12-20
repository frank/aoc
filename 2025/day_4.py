from pathlib import Path
from typing import Any
import numpy as np
from scipy.signal import convolve2d

TEST = False


def get_data() -> list[str]:
    day_n = Path(__file__).stem.split("_")[1]
    test_suffix = "_test" if TEST else ""
    fpath = Path(__file__).parent / "inputs" / f"day_{day_n}{test_suffix}.txt"
    with open(fpath, "r") as file:
        data = file.read().splitlines()
    return data


def process_data(data: list[str]) -> Any:
    data = np.array([[c for c in line] for line in data])
    data = (data == "@").astype(np.uint8)
    return data


def part_one(data):
    result = 0
    data_pad = np.pad(data, 1)
    kernel = np.ones((3, 3)).astype(data.dtype)
    kernel[1, 1] = 0
    conv = convolve2d(data_pad, kernel, mode="valid")
    result = np.sum(data.astype(bool) & (conv < 4))
    print("Part One:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 13 else "[FAILURE]")
    else:
        print()


def part_two(data):
    result = 0
    start_total = np.sum(data)

    old_n_rolls = 0
    while np.sum(data) != old_n_rolls:
        old_n_rolls = np.sum(data)
        data_pad = np.pad(data, 1)
        kernel = np.ones((3, 3)).astype(data.dtype)
        kernel[1, 1] = 0
        conv = convolve2d(data_pad, kernel, mode="valid")
        data = data - (data.astype(bool) & (conv < 4)).astype(np.uint8)

    result = start_total - np.sum(data)
    print("Part Two:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 43 else "[FAILURE]")
    else:
        print()


if __name__ == "__main__":
    data = get_data()
    data = process_data(data)
    part_one(data)
    part_two(data)
