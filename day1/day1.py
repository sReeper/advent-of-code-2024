from collections import Counter

left, right = [], []

with open("day1.input", "r") as input:
    for line in input:
        lv, rv = line.split("   ")
        left.append(int(lv))
        right.append(int(rv))

combined = zip(sorted(left), sorted(right))

distance = 0

for c in combined:
    distance += abs(c[0] - c[1])

print(distance)

count = Counter(right)
similarity = 0

for v in left:
    similarity += v * count.get(v, 0)

print(similarity)
