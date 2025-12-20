import numpy as np
from collections import Counter


def get_data() -> np.ndarray:
    with open("inputs/day_1.txt", "r") as file:
        lists = file.read()
    lists = [[int(n) for n in l.split("   ")] for l in lists.split("\n")]
    return np.array(lists).T


def main():
    lists = get_data()
    lists = np.sort(lists)
    counter = dict(Counter(lists[1].tolist()))
    result = np.sum([n * counter.get(n, 0) for n in lists[0].tolist()])
    print(result)


if __name__ == "__main__":
    main()
