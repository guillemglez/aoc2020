from typing import List, Dict, Tuple

SHINY = 'shiny gold'

with open('input') as f:
    inpt = f.read()

### PART 1

can: int = 0
could: int = 0
unchanged: bool = False
bags: List[str] = [SHINY]

while not unchanged:
    for line in inpt.split('\n'):
        for bag in bags.copy():
            if bag in line and not line.startswith(bag):
                other = line.split(' bags')[0]
                if other not in bags:
                    bags.append(other)
                    can += 1
    unchanged = (can - could) == 0
    if not unchanged:
        could = can

print(f'{can} bag types can carry a {SHINY} bag.')

### PART 2

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


def resolve(bag: str) -> int:
    total = 1
    for num, other in bagmap[bag]:
        total += num * resolve(other)
    return total

print(f"A {SHINY} bag must contain {resolve(SHINY) - 1} other bags.")
