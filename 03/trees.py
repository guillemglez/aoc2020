from typing import List

slopes: List[dict] = [{
    "x": 1,
    "y": 1
}, {
    "x": 3,
    "y": 1
}, {
    "x": 5,
    "y": 1
}, {
    "x": 7,
    "y": 1
}, {
    "x": 1,
    "y": 2
}]

for slope in slopes:
    slope["trees"] = 0
    slope["pos"] = 0

with open("input") as f:
    for i, line in enumerate(f):
        for slope in slopes:
            if (i % slope["y"]):
                continue

            char = slope["pos"] % (len(line) - 1)  # ignore \n

            if line[char] == "#":
                slope["trees"] += 1

            slope["pos"] += slope["x"]

product = 1
for slope in slopes:
    if slope["x"] == 3:
        trees = slope["trees"]
    product *= slope["trees"]

print(f"You have encountered {trees} trees following slope (3, 1)")
print(f"Second part result is {product}")
