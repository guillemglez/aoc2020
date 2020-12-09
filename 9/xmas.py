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

for i, number in enumerate(inpt):
    contiguous: List[int] = [number]
    while sum(contiguous) < invalid:
        contiguous.append(inpt[i + len(contiguous)])

    if sum(contiguous) == invalid:
        break

print(f"The fist number not sticking to the rule is {invalid}")
print(f"The encription weakness is {min(contiguous) + max(contiguous)}")
