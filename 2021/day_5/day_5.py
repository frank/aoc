import numpy as np


def get_inclusive_range(start, end):
    if start < end:
        return [x for x in range(start, end + 1)]
    elif start > end:
        return [x for x in range(end, start + 1)][::-1]
    else:
        return [start]


def draw_segment(segment_map, segment):
    p1, p2 = segment[0], segment[1]

    # check if non-diagonal
    if p1[0] == p2[0]:
        for p in [(p1[0], y) for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1)]:
            segment_map[p[0], p[1]] += 1
    elif p1[1] == p2[1]:
        for p in ((x, p1[1]) for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)):
            segment_map[p[0], p[1]] += 1
    else:
        for p in zip(
            get_inclusive_range(p1[0], p2[0]), get_inclusive_range(p1[1], p2[1])
        ):
            segment_map[p[0], p[1]] += 1

    return segment_map


segments = []

with open("input_day_5.txt", "r") as file:
    for line in (l.rstrip("\n") for l in file.readlines()):
        # get points
        p1, p2 = line.split(" -> ")
        segment = np.array(
            [[int(c) for c in p1.split(",")], [int(c) for c in p2.split(",")]]
        )

        # only keep vertical segments
        segments.append(segment)

segments = np.array(segments)

# initialize matrix representation
max_x = np.max(segments[..., 0]) + 1
max_y = np.max(segments[..., 1]) + 1
segment_map = np.zeros((max_x, max_y))

# draw segments
for segment in segments:
    segment_map = draw_segment(segment_map, segment)

print(f"Total spots with more than one line: {len(segment_map[segment_map > 1])}")
