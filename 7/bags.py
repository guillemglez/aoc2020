from typing import List

SHINY = 'shiny gold'

with open('input') as f:
    inpt = f.read()

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
