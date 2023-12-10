def get_data() -> list[list[int]]:
    with open("inputs/day_1.txt", "r") as file:
        calories = file.read()
    calories = calories.split("\n\n")
    calories = [[int(c) for c in cals.split("\n")] for cals in calories]
    return calories


def part_one(calories: list[list[int]]):
    result = max([sum(cals) for cals in calories])
    print(result)


def part_two(calories: list[list[int]]):
    result = sorted([sum(cals) for cals in calories], reverse=True)
    result = sum(result[:3])
    print(result)


if __name__ == "__main__":
    data = get_data()
    part_one(calories=data)
    part_two(calories=data)
