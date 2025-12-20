from pathlib import Path
from typing import Any
import numpy as np
from scipy.signal import convolve2d

TEST = False
PRINT = False

MAP = {".": 0, "S": 1, "^": -1}
RMAP = {
    0: ".",
    1: "|",
    -1: "^",
}


def print_map(data: np.ndarray, show_num: bool = False):
    print("=" * 30)
    if show_num:
        _rmap = RMAP.copy()
        del _rmap[1]
        _map = "\n".join(
            ["".join([_rmap.get(c, str(c)) for c in line]) for line in data]
        )
    else:
        _map = "\n".join(["".join([RMAP.get(c, "#") for c in line]) for line in data])
    print(_map)


def get_data() -> list[str]:
    day_n = Path(__file__).stem.split("_")[1]
    test_suffix = "_test" if TEST else ""
    fpath = Path(__file__).parent / "inputs" / f"day_{day_n}{test_suffix}.txt"
    with open(fpath, "r") as file:
        data = file.read().splitlines()
    return data


def process_data(data: list[str]) -> Any:
    processed = []
    for line in data:
        processed.append([MAP[c] for c in line])
    processed = np.array(processed)
    return processed


def current_row(data: np.ndarray):
    return np.max(np.where(data == 1)[0]).item()


def part_one(data):
    data = data.copy()
    result = 0

    # ray kernel should trigger when a ray can flow downwards
    ray_kernel = np.zeros((5, 5)).astype(data.dtype)
    ray_kernel[0, 2] = 1
    ray_kernel[1, 2] = 1
    ray_kernel = ray_kernel[::-1, ::-1]  # flip so we're doing a correlation

    # split kernel should handle bifurcations
    split_kernel = np.zeros((3, 3)).astype(data.dtype)
    split_kernel[0, 0] = 1
    split_kernel[1, 0] = -1
    split_kernel_l = split_kernel[
        ::-1, ::-1
    ].copy()  # flip so we're doing a correlation
    split_kernel_r = split_kernel[::-1].copy()

    for _ in range(len(data)):  # heuristic termination, capping iters at number of rows
        if PRINT:
            cr = current_row(data)
            print_map(data[max(0, cr - 5) : min(len(data), cr + 5)])

        old_data = data.copy()

        # propagate rays
        data_pad = np.pad(data.copy(), 2)
        ray_conv = convolve2d(data_pad, ray_kernel, mode="valid")
        ray_conv = ((ray_conv >= 1) & (data == 0)).astype(data.dtype)
        data += ray_conv

        # split_rays
        data_pad = np.pad(data.copy(), 1)
        split_conv_l = convolve2d(data_pad, split_kernel_l, mode="valid")
        split_conv_r = convolve2d(data_pad, split_kernel_r, mode="valid")
        split_conv = (((split_conv_l >= 2) | (split_conv_r >= 2)) & (data == 0)).astype(
            data.dtype
        )
        data += split_conv

        if PRINT:
            cr = current_row(data)
            print_map(data[max(0, cr - 5) : min(len(data), cr + 5)])
            input()

        if np.all(data == old_data):
            break

    # count result
    counting_kernel = np.zeros((3, 3)).astype(data.dtype)
    counting_kernel[0, 1] = 1
    counting_kernel[1, 1] = -1
    counting_kernel = counting_kernel[::-1, ::-1]

    data_pad = np.pad(data.copy(), 1)
    count_map = convolve2d(data_pad, counting_kernel, mode="valid")
    count_map = count_map == 2
    result = np.sum(count_map)

    print("Part One:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 21 else "[FAILURE]")
    else:
        print()

    return data


def part_two(data):
    result = 0
    for r in range(len(data) - 1):
        row = data[r]
        for c in range(len(row)):
            el = row[c]
            if el > 0:
                if data[r + 1, c] == -1:
                    data[r + 1, c - 1] += el
                    data[r + 1, c + 1] += el
                else:
                    data[r + 1, c] += el

    result = np.sum(data[-1])

    print("Part Two:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 40 else "[FAILURE]")
    else:
        print()


if __name__ == "__main__":
    data = get_data()
    data = process_data(data)
    part_one(data)
    part_two(data)
