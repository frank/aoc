from pathlib import Path
from typing import Any
import numpy as np
from itertools import combinations_with_replacement
from scipy.optimize import linprog

TEST = False
PRINT = False


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
        p = {}
        items = line.split()
        p["target"] = np.array([{".": 0, "#": 1}[char] for char in items[0][1:-1]])
        p["joltage"] = np.array([int(n) for n in items[-1][1:-1].split(",")])

        p["actions"] = []
        for item in items[1:-1]:
            idx = [int(n) for n in item[1:-1].split(",")]
            effect = np.zeros(len(p["target"]), dtype=int)
            effect[idx] = 1
            p["actions"].append(effect)

        p["actions"] = np.array(p["actions"])
        processed.append(p)

    return processed


def part_one(data):
    result = 0

    for problem in data:
        solved = False
        target = problem["target"]
        actions = problem["actions"]

        n = 0
        while not solved:
            n += 1
            for buttons in combinations_with_replacement(list(range(len(actions))), n):
                buttons = list(buttons)
                state = np.sum(actions[buttons], axis=0) % 2
                if np.all(state == target):
                    solved = True
                    if PRINT:
                        print(f"Solution: {n} ({', '.join([str(n) for n in buttons])})")
                    break

        result += n

    print("Part One:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 7 else "[FAILURE]")
    else:
        print()


def part_two(data):
    result = 0

    for problem in data:
        target = np.array(problem["joltage"]).astype(float)
        actions = np.array(problem["actions"]).astype(float)

        solution = linprog(
            np.ones(len(actions)),
            A_eq=actions.T,
            b_eq=target,
            method="highs",
            integrality=np.ones(len(actions)),
        )
        status = solution.status
        clicks = solution.x
        n_clicks = np.round(np.sum(clicks)).astype(int).item()

        if status != 0:
            print("Status:", status)

        if PRINT:
            print("Clicks:", clicks)
            print("N. clicks:", n_clicks)

        result += n_clicks

    print("Part Two:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 33 else "[FAILURE]")
    else:
        print()


if __name__ == "__main__":
    data = get_data()
    data = process_data(data)
    part_one(data)
    part_two(data)
