import numpy as np


def get_data() -> np.ndarray:
    with open("inputs/day_10.txt", "r") as file:
        cycles = [1]
        for line in (l.rstrip("\n") for l in file.readlines()):
            if line == "noop":
                cycles.append(0)
            else:
                val = int(line.split()[1])
                cycles.extend([0, val])
    return np.cumsum(cycles).astype(np.int32)


def part_one(cycles: np.ndarray):
    keypoints = np.array([20, 60, 100, 140, 180, 220], dtype=np.uint16)
    values = cycles[keypoints - 1]
    print(f"Sum of signal strengths: {np.sum(keypoints * values)}")


def part_two(cycles: np.ndarray):
    positions = np.mgrid[:6, :40][1].ravel()
    pixel_values = np.isclose(cycles[:240], positions, atol=1)
    pixels = ["#" if p else "." for p in pixel_values]
    [pixels.insert(idx, "\n") for idx in range(40, 246, 41)]
    print("".join(pixels))


if __name__ == "__main__":
    data = get_data()
    part_one(cycles=data)
    part_two(cycles=data)
