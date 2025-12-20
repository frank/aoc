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


def parse_shape(lines: list[str]):
    shape = []
    for line in lines:
        shape.append([(1 if c == "#" else 0) for c in line])
    return np.array(shape, dtype=int)


def process_data(data: list[str]) -> Any:
    processed = {"shapes": [], "sizes": [], "boxes": [], "contents": []}

    i = 0
    while data[i].endswith(":"):
        processed["shapes"].append(parse_shape(data[i + 1 : i + 4]))
        processed["sizes"].append(np.sum(processed["shapes"][-1]).item())
        i += 5

    for line in data[i:]:
        box, contents = line.split(": ")
        processed["boxes"].append(
            np.zeros([int(n) for n in box.split("x")], dtype=np.int64).T
        )
        processed["contents"].append([int(n) for n in contents.split()])

    return processed


def part_one(data):
    result = 0

    shapes = np.array(data["shapes"])
    boxes = data["boxes"]
    contents = np.array(data["contents"])
    for b, c in zip(boxes, contents):
        n_cells = np.prod(b.shape).item()
        cells_needed = np.sum(shapes * c[..., None, None])
        if n_cells >= cells_needed:
            result += 1

    print("Part One:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 2 else "[FAILURE]")
    else:
        print()


if __name__ == "__main__":
    data = get_data()
    data = process_data(data)
    part_one(data)
