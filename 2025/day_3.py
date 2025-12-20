from pathlib import Path
import numpy as np

TEST = False


def get_data() -> list[str]:
    day_n = Path(__file__).stem.split("_")[1]
    test_suffix = "_test" if TEST else ""
    fpath = Path(__file__).parent / "inputs" / f"day_{day_n}{test_suffix}.txt"
    with open(fpath, "r") as file:
        data = file.read().splitlines()
    return data


def process_data(data: list[str]) -> list[list[int]]:
    processed = []
    for el in data:
        numel = [int(c) for c in el]
        processed.append(numel)
    return processed


def part_one(data):
    result = 0

    for numel in data:
        tens_idx = np.argmax(numel[:-1])
        ones_idx = np.argmax(numel[tens_idx + 1 :]) + tens_idx + 1
        result += numel[tens_idx] * 10 + numel[ones_idx]

    print("Part One:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 357 else "[FAILURE]")
    else:
        print()


def part_two(data):
    result = 0
    n = 12
    for numel in data:
        indices = []
        indices.append(np.argmax(numel[: -n + 1]))
        for i in range(1, n - 1):
            sub_array = numel[indices[-1] + 1 : -(n - i) + 1]
            indices.append(np.argmax(sub_array) + indices[-1] + 1)
        sub_array = numel[indices[-1] + 1 :]
        indices.append(np.argmax(sub_array) + indices[-1] + 1)
        result += int("".join([str(numel[idx]) for idx in indices]))

    print("Part Two:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 3121910778619 else "[FAILURE]")
    else:
        print()


if __name__ == "__main__":
    data = get_data()
    data = process_data(data)
    part_one(data)
    part_two(data)
