def change_position(direction, amount, position):
	if direction == "forward":
		return position[0] + amount, position[1] + (position[2] * amount), position[2]
	elif direction == "down":
		return position[0], position[1], position[2] + amount
	elif direction == "up":
		return position[0], position[1], position[2] - amount
	else:
		print("Wrong direction boyo!")

position = (0, 0, 0)

with open("input_day_2.txt", "r") as file:
	for line in file.readlines():
		direction, amount = line.rstrip('\n').split(' ')
		position = change_position(direction, int(amount), position)

print(f"Total traveled distance is {position}, which multiplied is {position[0] * position[1]}")
