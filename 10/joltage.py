from typing import Dict

with open('input') as f:
    adapters = [int(x) for x in f.read().split()]

# Sort
adapters.sort()
# Add wall
adapters.insert(0, 0)
# Add phone
adapters.append(adapters[-1] + 3)

difference: Dict[int, int] = {i: 0 for i in range(1, 4)}
for adapter, jolts in enumerate(adapters):
    if adapter == 0:
        continue

    difference[jolts - adapters[adapter - 1]] += 1

print(
    f"The number of 1-jolt differences multiplied by the number of 3-jolt differences is {difference[1] * difference[3]}"
)
