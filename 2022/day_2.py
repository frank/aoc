import numpy as np
from numpy.typing import NDArray


def get_data_one() -> NDArray[int]:
    strategy_map = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    strategy = []
    with open("inputs/day_2.txt", "r") as file:
        for line in file.readlines():
            strategy.append([strategy_map[s] for s in line.rstrip("\n").split(" ")])
    strategy = np.array(strategy)
    return strategy


def get_data_two() -> NDArray[int]:
    strategy_map = {
        "A": 1,
        "B": 2,
        "C": 3
    }
    strategy = []
    with open("inputs/day_2.txt", "r") as file:
        for line in file.readlines():
            strategy.append([strategy_map.get(s, s) for s in line.rstrip("\n").split(" ")])
    strategy = np.array(strategy)

    # convert the strategy list to the same format as the first problem
    strategy[
        np.where(strategy[:, 1] == "X"), 1
    ] = np.mod(strategy[np.where(strategy[:, 1] == "X"), 0].astype("int32") - 2, 3) + 1
    strategy[np.where(strategy[:, 1] == "Y"), 1] = strategy[np.where(strategy[:, 1] == "Y"), 0]
    strategy[
        np.where(strategy[:, 1] == "Z"), 1
    ] = np.mod(strategy[np.where(strategy[:, 1] == "Z"), 0].astype("int32"), 3) + 1

    return strategy.astype("int64")


def count_scores(strategy: NDArray[int]):
    play_score = np.sum(strategy[:, 1])
    draw_score = np.sum(strategy[:, 0] == strategy[:, 1]) * 3
    rock_win_score = np.sum(np.min((strategy == [3, 1]), axis=1)) * 6
    paper_win_score = np.sum(np.min((strategy == [1, 2]), axis=1)) * 6
    scissors_win_score = np.sum(np.min((strategy == [2, 3]), axis=1)) * 6
    print(play_score + draw_score + rock_win_score + paper_win_score + scissors_win_score)


if __name__ == "__main__":
    data = get_data_one()
    count_scores(strategy=data)
    data = get_data_two()
    count_scores(strategy=data)
