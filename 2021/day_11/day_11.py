import numpy as np


def adj_finder(matrix, position):
    adj = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            range_x = range(0, matrix.shape[0])
            range_y = range(0, matrix.shape[1])
            (new_x, new_y) = (position[0] + dx, position[1] + dy)
            if (new_x in range_x) and (new_y in range_y) and (dx, dy) != (0, 0):
                adj.append((new_x, new_y))
    return adj


field = []
with open("text_input.txt", "r") as file:
    for line in (l.rstrip('\n') for l in file.readlines()):
        field.append([int(n) for n in line])

field = np.array(field)
n_flashes = 0


def flash():
    global n_flashes
    while np.any(field > 9):
        flashing = list(zip(np.where(field > 9)[0], np.where(field > 9)[1]))
        for x, y in flashing:
            adj = adj_finder(field, (x, y))
            for p in adj:
                field[p[0], p[1]] += 1
    for x, y in list(zip(np.where(field > 9)[0], np.where(field > 9)[1])):
        field[x, y] = 0
        n_flashes += 1


for i in range(5):
    print(field)
    field += 1
    flash()

print(field)

print(f"Total flashes: {n_flashes}")
