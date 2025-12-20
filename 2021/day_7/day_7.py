from functools import lru_cache

import numpy as np
from tqdm import tqdm


@lru_cache(maxsize=None)
def get_path_cost(n):
    total = np.ulonglong(0)
    for i in range(n):
        total += i + 1
    return total


def get_fuel_consumption(positions, center):
    fuel = 0
    for pos in positions:
        distance = pos - center if pos > center else center - pos
        fuel += get_path_cost(distance)
    return int(fuel)


with open("input_day_7.txt", "r") as file:
    positions = np.array([int(nr) for nr in file.read().split(",")])

min_fuel = None
for i in tqdm(range(max(positions)), total=max(positions), ascii=True, ncols=70):
    fuel = get_fuel_consumption(positions, i)
    if min_fuel is None or min_fuel > fuel:
        min_fuel = fuel
        final_pos = i

print(f"Minimum fuel used is {min_fuel} at position {final_pos}")
