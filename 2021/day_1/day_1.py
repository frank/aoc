with open("input_day_1.txt", "r") as file:
    readings = [int(line.rstrip('\n')) for line in file.readlines()]


def get_list_change(lst):
    return [lst[i] - lst[i - 1] for i in range(1, len(lst))]


readings_change = get_list_change(readings)
print(f"Number of increasing readings: {sum(1 for item in readings_change if item > 0)}")

sw_readings = [sum(readings[i:i + 3]) for i in range(len(readings) - 2)]
sw_readings_change = get_list_change(sw_readings)
print(f"Number of increasing 3-sliding window readings: {sum(1 for item in sw_readings_change if item > 0)}")
