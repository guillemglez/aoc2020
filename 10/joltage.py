from typing import Dict, List

with open('input') as f:
    adapters = [int(x) for x in f.read().split()]

# Sort
adapters.sort()
# Add wall
adapters.insert(0, 0)
# Add phone
adapters.append(adapters[-1] + 3)

differences: Dict[int, int] = {i: 0 for i in range(1, 4)}
derivative: List[int] = []
for adapter, jolts in enumerate(adapters):
    if adapter == 0:
        continue

    differences[jolts - adapters[adapter - 1]] += 1
    derivative.append(jolts - adapters[adapter - 1])


# Thanks to Pietro Peterlongo :)
# https://pietroppeter.github.io/adventofnim/2020/day10hints.html
def possibilities(derivative: List[int]) -> int:

    # There is a single possibility for a two-element sequence
    if len(derivative) < 2:
        return 1
    # There are two possibilities in a three element sequence (2 or 3 elements), except if there is a 3-valued derivative, which is blocking
    if len(derivative) == 2:
        return 2 if 3 not in derivative else 1

    # Initial/final 3 or 2,2 differences won't change the output, remove them
    if derivative[0] == 3:
        return possibilities(derivative[1:])
    if derivative[-1] == 3:
        return possibilities(derivative[:-1])
    if derivative[0] == 2 and derivative[1] == 2:
        return possibilities(derivative[2:])
    if derivative[-1] == 2 and derivative[-2] == 2:
        return possibilities(derivative[:-2])

    # Where there is a derivative of three, the sequence may be split
    for i, d in enumerate(derivative):
        if d == 3:
            return possibilities(derivative[:i]) * possibilities(
                derivative[i + 1:])

    # Where there is a derivative of two consecutive 2s, the sequence may be split
    for i, d in enumerate(derivative[:-2]):
        if d == 2 and derivative[i + 1] == 2:
            return possibilities(derivative[:i]) * possibilities(
                derivative[i + 2:])

    # [x y sequence] === [y sequence] + [x+y sequence]
    # Keep shortening this way until a length of 2
    return possibilities(
        derivative[1:]) + possibilities([sum(derivative[:2])] + derivative[2:])


print(
    f"The number of 1-jolt differences multiplied by the number of 3-jolt differences is {differences[1] * differences[3]}"
)
print(f"There are {possibilities(derivative)} distinct arrangements.")
