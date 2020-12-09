from typing import List

with open('input') as f:
    inpt = [int(x) for x in f.read().split()]

header: List[int] = []

for number in inpt:
    if len(header) < 25:
        header.append(number)
        continue

    valid: List[int] = []
    for one in header:
        for another in header:
            if not one == another:
                valid.append(one + another)

    if number not in valid:
        invalid = number
        break

    header.pop(0)
    header.append(number)

print(f"The fist number not sticking to the rule is {invalid}")
