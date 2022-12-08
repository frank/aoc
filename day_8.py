import numpy as np
from itertools import product


def get_data() -> np.ndarray:
    trees = []
    with open("inputs/day_8.txt", "r") as file:
        trees = [[int(tree) for tree in line.rstrip("\n")] for line in file.readlines()]
    return np.array(trees)


def part_one(trees: np.ndarray):
    visibility_map = np.zeros_like(trees)
    visibility_map[0, :] = 1
    visibility_map[-1, :] = 1
    visibility_map[:, 0] = 1
    visibility_map[:, -1] = 1
    for r, c in product(range(1, trees.shape[0] - 1), range(1, trees.shape[1] - 1)):
        n = np.all(trees[:r, c] < trees[r, c])
        s = np.all(trees[r + 1:, c] < trees[r, c])
        w = np.all(trees[r, :c] < trees[r, c])
        e = np.all(trees[r, c + 1:] < trees[r, c])
        visible = n or s or w or e
        if visible:
            visibility_map[r, c] = 1
    print(np.sum(visibility_map))


def part_two(trees: np.ndarray):
    scenic_map = np.zeros_like(trees)
    for r, c in product(range(trees.shape[0]), range(trees.shape[1])):
        ...


if __name__ == "__main__":
    data = get_data()
    part_one(trees=data)
