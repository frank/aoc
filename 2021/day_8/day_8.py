def get_ground_keys(codes):
    keys = {}
    for code in (set(c) for c in codes):
        if len(code) == 2:
            keys[1] = code
        elif len(code) == 4:
            keys[4] = code
        elif len(code) == 3:
            keys[7] = code
        elif len(code) == 7:
            keys[8] = code
    return keys


def get_remaining_keys(codes, cypher):
    keys = {}
    bottomleft_corner = cypher[8] - (cypher[4] | cypher[7])
    for code in (set(c) for c in codes):
        if len(code) == 6 and (bottomleft_corner | cypher[1]).issubset(code):
            keys[0] = code
        elif len(code) == 5 and bottomleft_corner.issubset(code):
            keys[2] = code
        elif len(code) == 5 and cypher[1].issubset(code):
            keys[3] = code
        elif len(code) == 5 and (cypher[4] - cypher[1]).issubset(code):
            keys[5] = code
        elif len(code) == 6 and (bottomleft_corner | (cypher[4] - cypher[7])).issubset(code):
            keys[6] = code
        elif len(code) == 6 and (cypher[4]).issubset(code):
            keys[9] = code
    return keys


def translate_digits(code, cypher):
    digits = ''
    for d in code:
        digits += str(next(key for key, value in cypher.items() if value == set(d)))
    return int(digits)


signals = []
with open("input_day_8.txt", "r") as file:
    for code, digits in (line.rstrip('\n').split(' | ') for line in file.readlines()):
        signal = {
            "code": code.split(),
            "digits": digits.split()
        }
        signals.append(signal)

count = 0
for signal in signals:
    cypher = {}
    cypher.update(get_ground_keys(signal["code"]))
    cypher.update(get_remaining_keys(signal["code"], cypher))
    number = translate_digits(signal["digits"], cypher)
    count += number

print(f"Total number sum: {count}")
