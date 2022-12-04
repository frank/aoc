import numpy as np


def get_data_one() -> list[tuple[list[str], list[str]]]:
    sacks = []
    with open("inputs/day_3.txt", "r") as file:
        for line in file.readlines():
            line = line.rstrip("\n")
            a, b = line[:len(line) // 2], line[len(line) // 2:]
            sacks.append((list(a), list(b)))
    return sacks


def get_data_two() -> list[set[str]]:
    sacks = []
    with open("inputs/day_3.txt", "r") as file:
        for line in file.readlines():
            line = line.rstrip("\n")
            sacks.append(set(line))
    return sacks


def part_one(sacks: list[tuple[list[str], list[str]]]):
    items = [list(set(a).intersection(set(b))) for (a, b) in sacks]
    assert np.all([len(i) == 1 for i in items])  # check it's one item per sack
    priorities = [ord(c[0]) - 96 if c[0].islower() else ord(c[0]) - 38 for c in items]
    print(sum(priorities))


def part_two(sacks: list[set[str]]):
    badges = [list(sacks[i].intersection(sacks[i + 1]).intersection(sacks[i + 2])) for i in range(0, len(sacks), 3)]
    assert np.all([len(i) == 1 for i in badges])  # check it's one badge per sack
    priorities = [ord(c[0]) - 96 if c[0].islower() else ord(c[0]) - 38 for c in badges]
    print(sum(priorities))


if __name__ == "__main__":
    data = get_data_one()
    part_one(sacks=data)
    data = get_data_two()
    part_two(sacks=data)
