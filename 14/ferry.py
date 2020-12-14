from typing import Tuple, Dict


def readmask(mask: str) -> Tuple[int, int]:
    lowmask, highmask = 0, 0
    for i, char in enumerate(mask):
        if char == '0':
            lowmask += 2**(35 - i)
        if char == '1':
            highmask += 2**(35 - i)
    return lowmask, highmask


def applymask(value: int, mask: Tuple[int, int]) -> int:
    lowmask, highmask = mask
    value |= highmask
    value &= ~lowmask
    return value


mem: Dict[int, int] = {}
with open('input') as f:
    for line in f:
        if 'mask' in line:
            mask = readmask(line.split('=')[1].strip())
        if 'mem' in line:
            address = int(line[line.find('[') + 1:line.find(']')])
            value = int(line.split('=')[1].strip())
            mem[address] = applymask(value, mask)

print(
    f"The sum of all values left in memory after it completes is {sum(mem.values())}"
)
