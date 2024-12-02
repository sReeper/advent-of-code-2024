def is_safe(entry):
    dampener = 1
    increasing = entry[0] > entry[1]

    for i in range(0, len(entry) - 1):
        if not (
            0 < abs(entry[i] - entry[i + 1]) <= 3
            and increasing == (entry[i] > entry[i + 1])
        ):
            if dampener <= 0:
                return False
            dampener -= 1

    return True


safe = 0

with open("day2.input", "r") as input:
    for line in input:
        entry = [int(x) for x in line.split(" ")]
        safe += 1 if is_safe(entry) else 0

print(safe)
