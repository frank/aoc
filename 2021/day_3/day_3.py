import numpy as np


def bool2int(x):
    return x.dot(1 << np.arange(x.shape[-1] - 1, -1, -1))


all_readings = []

with open("input_day_3.txt", "r") as file:
    for line in file.readlines():
        all_readings.append(np.array([int(c) for c in line.rstrip('\n')]))

all_readings = np.array(all_readings)

gamma_bin = (np.mean(all_readings, axis=0) >= 0.5).astype(int)
epsilon_bin = (gamma_bin == 0).astype(int)


def find_best_match(rdngs, match):
    pos = 0
    while len(rdngs) > 1:
        if match == "gamma":
            match_bin = (np.mean(rdngs, axis=0) >= 0.5).astype(int)
        elif match == "epsilon":
            match_bin = (np.mean(rdngs, axis=0) < 0.5).astype(int)
        rdngs = rdngs[rdngs[:, pos] == match_bin[pos], :]
        pos += 1

    assert len(rdngs) == 1
    return rdngs[0].dot(1 << np.arange(rdngs[0].shape[-1] - 1, -1, -1))


oxygen = find_best_match(all_readings.copy(), "gamma")
co2 = find_best_match(all_readings.copy(), "epsilon")

print(f"Oxygen: {oxygen}, CO2: {co2}, life support rating: {oxygen * co2}")
