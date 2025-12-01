import numpy as np


def is_bingo(matrices, location):
    row = matrices[location[0], location[1], :]
    column = matrices[location[0], :, location[2]]
    return sum(row) == - len(row) or sum(column) == - len(column)


matrices = []

with open("input_day_4.txt", "r") as file:
    lines = iter(file.readlines())
    called_nrs = [int(nr) for nr in next(lines).rstrip('\n').split(',')]
    _ = next(lines)
    matrix = []
    for line in lines:
        if not line.rstrip('\n'):
            matrices.append(matrix)
            matrix = []
        else:
            matrix.append([int(nr) for nr in line.rstrip('\n').split()])

matrices = np.array(matrices)

win_record = np.ones(len(matrices))
result = None
for nr in called_nrs:
    locations = np.argwhere(matrices == nr)
    for location in locations:
        matrices[location[0], location[1], location[2]] = -1
        if is_bingo(matrices, location) and win_record[location[0]] == 1:
            win_record[location[0]] = 0
            last_nr = nr
            matrix = matrices[location[0]]
            matrix[matrix == -1] = 0
            matrix_sum = np.sum(matrix)
            result = matrix_sum * last_nr

print(f"The result is {matrix_sum} * {last_nr} = {result}")
