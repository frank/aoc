import numpy as np

height_map = []
with open("input_day_9.txt", "r") as file:
    for line in (l.rstrip("\n") for l in file.readlines()):
        height_map.append(np.array([int(n) for n in line]))

height_map = np.array(height_map)

# make maps displaced by 1 in each direction
up = height_map.copy()
up[1:] -= up[:-1]
up[0] = -1
up = up < 0

down = height_map.copy()
down[:-1] -= down[1:]
down[-1] = -1
down = down < 0

left = height_map.copy()
left[:, 1:] -= left[:, :-1]
left[:, 0] = -1
left = left < 0

right = height_map.copy()
right[:, :-1] -= right[:, 1:]
right[:, -1] = -1
right = right < 0

# find minima
minima = up & down & left & right

# walls are 0s and basins are 1s
basin_map = (height_map < 9).astype(int)


def count_basin(x, y):
    # recursively count the basin
    count = 0
    basin_map[x, y] = 0

    if x > 0 and basin_map[x - 1, y]:
        count += count_basin(x - 1, y)
    if x + 1 < basin_map.shape[0] and basin_map[x + 1, y]:
        count += count_basin(x + 1, y)
    if y > 0 and basin_map[x, y - 1]:
        count += count_basin(x, y - 1)
    if y + 1 < basin_map.shape[1] and basin_map[x, y + 1]:
        count += count_basin(x, y + 1)

    return count + 1


# iterate over minima (and as such basins)
basins = []
for x, y in zip(np.where(minima)[0], np.where(minima)[1]):
    basins.append(count_basin(x, y))

basins = sorted(basins)[::-1]
print(f"Top three basins: {basins[0]}, {basins[1]}, {basins[2]}")
print(f"Product: {basins[0] * basins[1] * basins[2]}")
