from typing import List, Dict, Tuple

SHINY = 'shiny gold'

with open('input') as f:
    inpt = f.read()

bagmap: Dict[str, List[Tuple[int, str]]] = {}
for line in inpt.split('\n'):
    if not 'bags' in line:
        continue
    this = line.split(' bags')[0]
    bagmap[this] = []
    if 'no other bags' in line:
        continue
    for rule in line.split('contain ')[1].split(', '):
        num = int(rule.split()[0])
        bag = ' '.join(rule.split()[1:-1])
        bagmap[this].append((num, bag))


def carry(target: str) -> int:
    total = 1
    for carrier, carried in bagmap.copy().items():
        for num, bag in carried:
            if bag == target:
                bagmap.pop(carrier)
                total += carry(carrier)
                break
    return total


def contains(bag: str) -> int:
    total = 1
    for num, other in bagmap[bag]:
        total += num * contains(other)
    return total


print(f'{carry(SHINY) - 1} bag types can carry a {SHINY} bag.')
print(f"A {SHINY} bag must contain {contains(SHINY) - 1} other bags.")
