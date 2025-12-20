from pathlib import Path
from typing import Any
import numpy as np
import cv2
from time import time

TEST = False


def get_data() -> list[str]:
    day_n = Path(__file__).stem.split("_")[1]
    test_suffix = "_test" if TEST else ""
    fpath = Path(__file__).parent / "inputs" / f"day_{day_n}{test_suffix}.txt"
    with open(fpath, "r") as file:
        data = file.read().splitlines()
    return data


def process_data(data: list[str]) -> Any:
    processed = [[float(n) for n in line.split(",")] for line in data]
    processed = np.array(processed)
    return processed


def print_map(tiles_img: np.ndarray):
    if not TEST:
        print("Not printing full map.")
    print("=" * 30)
    d = {True: "#", False: "."}
    _map = "\n".join(["".join([d[c] for c in line]) for line in tiles_img])
    print(_map)


def part_one(data):
    result = 0

    data[:, 0] -= np.min(data[:, 0])
    data[:, 1] -= np.min(data[:, 1])

    x_diffs = np.abs(np.subtract.outer(data[:, 0], data[:, 0]) + 1) - np.eye(len(data))
    y_diffs = np.abs(np.subtract.outer(data[:, 1], data[:, 1]) + 1) - np.eye(len(data))
    areas = x_diffs * y_diffs

    result = int(np.max(areas))

    print("Part One:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 50 else "[FAILURE]")
    else:
        print()


def part_two(data):
    s = time()
    result = 0

    data = np.fliplr(data)
    data[:, 0] -= np.min(data[:, 0]) - 1
    data[:, 1] -= np.min(data[:, 1]) - 1

    img = np.zeros(
        (int(np.max(data[:, 0])) + 2, int(np.max(data[:, 1])) + 2), dtype=bool
    )
    for i in range(len(data) - 1):
        indices = np.linspace(
            data[i], data[i + 1], int(np.max(np.abs(data[i] - data[i + 1]))) + 1
        ).astype(int)
        img[indices[:, 0], indices[:, 1]] = True
    indices = np.linspace(
        data[-1], data[0], int(np.max(np.abs(data[-1] - data[0]))) + 1
    ).astype(int)
    img[indices[:, 0], indices[:, 1]] = True

    print("Filling polygon...")
    img = img.astype(np.uint8)
    cv2.fillPoly(img, [np.fliplr(data.astype(int))], color=(1))
    img = img.astype(bool)

    x_diffs = np.abs(np.subtract.outer(data[:, 0], data[:, 0])) + 1 - np.eye(len(data))
    y_diffs = np.abs(np.subtract.outer(data[:, 1], data[:, 1])) + 1 - np.eye(len(data))
    areas = x_diffs * y_diffs

    i = 0
    while not result:
        index = np.argmax(areas).item()

        print(f"Checking {i}", end="\r")

        c = np.stack([data[index // len(data)], data[index % len(data)]]).astype(int)

        if np.all(img[np.min(c[:, 0]) : np.max(c[:, 0]) + 1, c[:, 1]]) and np.all(
            img[c[:, 0], np.min(c[:, 1]) : np.max(c[:, 1]) + 1]
        ):
            result = int(np.max(areas))

        areas[index // len(data), index % len(data)] = 0
        areas[index % len(data), index // len(data)] = 0

        i += 1
    print()

    print(f"Elapsed: {time() - s:.2f}s")
    print("Part Two:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 24 else "[FAILURE]")
    else:
        print()


if __name__ == "__main__":
    data = get_data()
    data = process_data(data)
    part_one(data.copy())
    part_two(data.copy())
