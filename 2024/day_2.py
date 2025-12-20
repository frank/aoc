import numpy as np


def get_data():
    with open("inputs/day_2.txt", "r") as file:
        data = file.read()
    data = [[int(c) for c in r.split(" ")] for r in data.split("\n")]
    return data


def is_safe(row):
    dampener = True
    diff = np.diff(row)
    prev = row[0]
    for l in zip(row[1:], diff):
        if prev * l < 0:
            return False
        dif = abs(prev - l)
        if dif > 3 or dif < 1:
            return False
        prev = l
    return True


def main():
    data = get_data()
    n_safe = 0
    for d in data:
        print(d)
        if is_safe(d):
            print("safe")
            n_safe += 1
    print(n_safe)


if __name__ == "__main__":
    main()
