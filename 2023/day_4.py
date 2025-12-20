def get_data() -> list[list[set[int]]]:
    assignments = []
    with open("inputs/day_4.txt", "r") as file:
        for line in file.readlines():
            assignments.append(
                [
                    set(range(int(s.split("-")[0]), int(s.split("-")[1]) + 1))
                    for s in line.rstrip("\n").split(",")
                ]
            )
    return assignments


def part_one(assignments: list[list[set[int]]]):
    subsumed = [a.issubset(b) or b.issubset(a) for (a, b) in assignments]
    print(sum(subsumed))


def part_two(assignments: list[list[set[int]]]):
    overlaps = [not a.isdisjoint(b) for (a, b) in assignments]
    print(sum(overlaps))


if __name__ == "__main__":
    data = get_data()
    part_one(assignments=data)
    part_two(assignments=data)
