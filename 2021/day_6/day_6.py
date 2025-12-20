import numpy as np

with open("input_day_6.txt", "r") as file:
    timers = np.array([int(nr) for nr in file.read().split(",")])

timers = np.array([np.count_nonzero(timers == i) for i in range(9)], dtype=np.ulonglong)

n_days = 256
for day_idx in range(n_days):
    n_new = timers[0]
    timers = np.concatenate((timers[1:], [timers[0]]))
    timers[6] += n_new

print(f"Fish after {n_days} days: {int(sum(timers))}")
