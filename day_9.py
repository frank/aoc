import numpy as np


def get_data() -> np.ndarray:
    # using cartesian coordinates and axes' orientations
    directions = {
        "R": [1, 0],
        "L": [-1, 0],
        "U": [0, 1],
        "D": [0, -1],
    }
    with open("inputs/day_9.txt", "r") as file:
        steps = []
        for line in file.readlines():
            direction, iters = line.rstrip("\n").split()
            for _ in range(int(iters)):
                steps.append(directions[direction])
    return np.array(steps)


def tail_step(head: np.ndarray, tail: np.ndarray):
    if np.all(np.abs(head - tail) <= 1):
        return np.array([0, 0])
    return np.clip(head - tail, a_min=-1, a_max=1)


def part_one(steps: np.ndarray, n_knots: int = 1):
    rope = [np.array([0, 0])]
    for k in range(n_knots):
        rope.append(np.array([0, 0]))
    visited_states = {tuple(rope[-1])}
    for s in steps:
        rope[0] += s
        for k in range(n_knots):
            rope[k + 1] += tail_step(rope[k], rope[k + 1])
        visited_states.add(tuple(rope[-1]))
    print(f"Tail with {n_knots} knots visited {len(visited_states)} states")


if __name__ == "__main__":
    data = get_data()
    part_one(steps=data)
    part_one(steps=data, n_knots=9)
