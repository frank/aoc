import statistics

rows = []
with open("input_day_10.txt", "r") as file:
    for line in (l.rstrip('\n') for l in file.readlines()):
        rows.append(line)

opening_chars = '([{<'
closing_chars = ')]}>'
all_chars = opening_chars + closing_chars

match = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

inv_match = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

inv_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

score = 0
closing_rows = []
for row in rows:
    log = []
    for char in row:
        if char in opening_chars:
            log.append(char)
        elif char in closing_chars:
            if log[-1] == match[char]:
                log = log[:-1]
            else:
                score += points[char]
                log = []
                break
    if log:
        closing_rows.append([inv_match[c] for c in log[::-1]])

print(f"Total points: {score}")

closing_scores = []
for crow in closing_rows:
    score = 0
    for c in crow:
        score *= 5
        score += inv_points[c]
    closing_scores.append(score)

print(f"Median score: {sorted(closing_scores)[len(closing_scores) // 2]}")
