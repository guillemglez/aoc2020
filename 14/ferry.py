from typing import Tuple, Dict, List


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


def readfmask(mask: str) -> int:
    fmask = 0
    for i, char in enumerate(mask):
        if char == 'X':
            fmask += 1 << (35 - i)
    return fmask


def applyfmask(faddress: int, fmask: int) -> List[int]:
    indexes: List[int] = []
    for b in range(36):
        if fmask & 1 << b:
            indexes.append(b)
    addresses: List[int] = []
    for i in range(1 << len(indexes)):
        address = faddress
        for b in range(len(indexes)):
            if i & 1 << b:
                address |= 1 << indexes[b]
            else:
                address &= ~(1 << indexes[b])
        addresses.append(address)
    return addresses


mem.clear()
with open('input') as f:
    for line in f:
        if 'mask' in line:
            # Discard lowmask, since now 0s become unchanged
            mask = 0, readmask(line.split('=')[1].strip())[1]
            fmask = readfmask(line.split('=')[1].strip())
        if 'mem' in line:
            rawaddress = int(line[line.find('[') + 1:line.find(']')])
            faddress = applymask(rawaddress, mask)
            value = int(line.split('=')[1].strip())
            for address in applyfmask(faddress, fmask):
                mem[address] = value

print(
    f"Following the second version, the sum of all values is {sum(mem.values())}"
)
