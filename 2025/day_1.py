from pathlib import Path
from typing import Any


def get_data() -> list[str]:
    day_n = Path(__file__).stem.split("_")[1]
    fpath = Path(__file__).parent / "inputs" / f"day_{day_n}.txt"
    with open(fpath, "r") as file:
        data = file.read().splitlines()
    return data


def to_number(x: str) -> int:
    return int(x[1:]) * (-1 if x[0] == "L" else 1)


def process_data(data: list[str]) -> Any:
    data = [to_number(n) for n in data]
    return data


def part_one(data: list[int]):
    current = 50
    zeros = 0
    for n in data:
        current = (current + n) % 100
        if current == 0:
            zeros += 1
    print("Part One:", zeros)


def part_two(data: list[int]):
    current = 50
    zeros = 0
    for n in data:
        new = current + n

        # print("---")
        # print(f"{current} {'-' if n < 0 else '+'} {abs(n)} -> {new}", end="")
        # print("" if (new % 100) == new else f" -> {(new % 100)}")

        turned_negative = current * new < 0
        z = (abs(new) + (100 if turned_negative else 0)) // 100
        if new == 0:
            z += 1

        # if z:
        #     print("Adding", z)

        zeros += z
        current = new % 100
    print("Part Two:", zeros)


if __name__ == "__main__":
    data = get_data()
    data = process_data(data)
    part_one(data)
    part_two(data)
