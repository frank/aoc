import string
from collections import deque

import numpy as np


def get_data() -> tuple[list[deque], list[tuple[int]]]:
    with open("inputs/day_5.txt", "r") as file:
        lines = file.readlines()
        separator = lines.index("\n")

        # make stacks
        stacks = []
        for i in range(separator):
            stacks.append([c for c in lines[i].rstrip("\n")])
        stacks = np.array(stacks).T[:, ::-1]
        stacks = stacks[np.where(stacks[:, 0] != " "), 1:].squeeze()
        stacks = [deque([item for item in s if item != " "]) for s in stacks]

        # make instruction list
        instructions = []
        remove_text = str.maketrans("", "", string.ascii_lowercase)
        for i in range(separator + 1, len(lines)):
            numbers = [
                int(n) for n in lines[i].rstrip("\n").translate(remove_text).split()
            ]
            numbers[1] -= 1
            numbers[2] -= 1
            instructions.append(tuple(numbers))

    return stacks, instructions


def part_one(stacks: list[deque], instructions: list[tuple[int]]):
    for ins in instructions:
        for n in range(ins[0]):
            item = stacks[ins[1]].pop()
            stacks[ins[2]].append(item)
    print("".join([s[-1] for s in stacks]))


def part_two(stacks: list[deque], instructions: list[tuple[int]]):
    for ins in instructions:
        substack = [stacks[ins[1]].pop() for i in range(ins[0])]
        for item in substack[::-1]:
            stacks[ins[2]].append(item)
    print("".join([s[-1] for s in stacks]))


if __name__ == "__main__":
    stacks, instructions = get_data()
    part_one(stacks=stacks, instructions=instructions)
    stacks, instructions = get_data()
    part_two(stacks=stacks, instructions=instructions)
