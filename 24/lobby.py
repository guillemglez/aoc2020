from typing import List, Optional
import numpy as np


def vector(cardinal: str) -> np.array:
    if cardinal == 'e':
        return np.array([0, 2])
    if cardinal == 'w':
        return np.array([0, -2])
    if cardinal == 'ne':
        return np.array([-1, 1])
    if cardinal == 'nw':
        return np.array([-1, -1])
    if cardinal == 'se':
        return np.array([1, 1])
    if cardinal == 'sw':
        return np.array([1, -1])


tiles: List[np.array] = []
with open('input') as f:
    for line in f:
        last: Optional[str] = None
        direction = np.array([0, 0])
        for cardinal in line:
            if cardinal == 'n' or cardinal == 's':
                last = cardinal
                continue
            elif cardinal == 'e' or cardinal == 'w':
                if last:
                    cardinal = last + cardinal
                    last = None
                direction += vector(cardinal)

        tiles.append(direction)

radius = max([np.hypot(*direction) for direction in tiles])
lobby = np.zeros((int(radius * 2 + 1), ) * 2, dtype=bool)
central = tuple(s // 2 for s in lobby.shape)

for tile in tiles:
    row, col = tile
    crow, ccol = central
    lobby[row + crow, col + ccol] = not lobby[row + crow, col + ccol]

print(f"There are {np.count_nonzero(lobby)} tiles left with the black side up")
