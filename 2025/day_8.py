from pathlib import Path
from typing import Any
from scipy.spatial.distance import cdist
import numpy as np

TEST = False


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
        processed.append([float(n) for n in line.split(",")])
    return processed


def get_groups(node_a: int, node_b: int, groups: list[set]) -> int:
    gs = {node_a: None, node_b: None}
    for s in range(len(groups)):
        if node_a in groups[s]:
            gs[node_a] = s
        if node_b in groups[s]:
            gs[node_b] = s
        if gs[node_a] is not None and gs[node_b] is not None:
            break
    return list(set([g for g in gs.values() if g is not None]))


def part_one(data):
    result = 0

    n_nodes = len(data)
    distance_matrix = cdist(data, data)
    limit = np.round(np.max(distance_matrix) + 10)
    distance_matrix += np.eye(len(distance_matrix)) * limit

    groups = []
    n_iters = 10 if TEST else 1000
    for _ in range(n_iters):
        idx = np.argmin(distance_matrix)
        # get row, col index. can be swapped since the matrix is symmetrical
        idx = (idx // n_nodes).item(), (idx % n_nodes).item()

        matches = get_groups(*idx, groups)
        if len(matches) > 2:
            raise ValueError(f"get_groups returned {len(matches)} groups")

        if len(matches) == 0:
            # make a new group
            groups.append(set({*idx}))
        elif len(matches) == 1:
            m = matches[0]
            groups[m] = groups[m].union(set({*idx}))
        elif len(matches) == 2:
            m1, m2 = matches
            groups[m1] = groups[m1].union(groups[m2])
            del groups[m2]

        # make sure this link doesn't trigger again
        distance_matrix[*idx] = limit
        distance_matrix[*idx[::-1]] = limit

        if not np.any(distance_matrix != limit):
            break

    groups = sorted(groups, key=lambda x: len(x), reverse=True)
    result = len(groups[0]) * len(groups[1]) * len(groups[2])

    print("Part One:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 40 else "[FAILURE]")
    else:
        print()


def part_two(data):
    result = 0

    n_nodes = len(data)
    distance_matrix = cdist(data, data)
    limit = np.round(np.max(distance_matrix) + 10)
    distance_matrix += np.eye(len(distance_matrix)) * limit

    groups = []
    while np.any(distance_matrix != limit):
        idx = np.argmin(distance_matrix)
        # get row, col index. can be swapped since the matrix is symmetrical
        idx = (idx // n_nodes).item(), (idx % n_nodes).item()

        matches = get_groups(*idx, groups)
        if len(matches) > 2:
            raise ValueError(f"get_groups returned {len(matches)} groups")

        if len(matches) == 0:
            # make a new group
            groups.append(set({*idx}))
        elif len(matches) == 1:
            m = matches[0]
            groups[m] = groups[m].union(set({*idx}))
        elif len(matches) == 2:
            m1, m2 = matches
            groups[m1] = groups[m1].union(groups[m2])
            del groups[m2]

        # make sure this link doesn't trigger again
        distance_matrix[*idx] = limit
        distance_matrix[*idx[::-1]] = limit

        if len(groups) == 1 and len(groups[0]) == n_nodes:
            break

    result = int(data[idx[0]][0]) * int(data[idx[1]][0])

    print("Part Two:", result, end=" ")
    if TEST:
        print("[SUCCESS]" if result == 25272 else "[FAILURE]")
    else:
        print()


if __name__ == "__main__":
    data = get_data()
    data = process_data(data)
    part_one(data)
    part_two(data)
