from typing import List, Optional
import numpy as np

BLACK = True
WHITE = False
DAYS = 100


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
lobby = np.zeros((int(radius * 2 + DAYS * 2 + 1), ) * 2, dtype=bool)
central = tuple(s // 2 for s in lobby.shape)

for tile in tiles:
    row, col = tile
    crow, ccol = central
    lobby[row + crow, col + ccol] = not lobby[row + crow, col + ccol]

print(
    f"There are {np.count_nonzero(lobby)} tiles left with the black side up after the instructions have been followed"
)

for day in range(DAYS):
    yesterday = lobby.copy()
    for idx, tile in np.ndenumerate(yesterday):
        row, col = idx
        black = 0
        if (row - 1) >= 0:
            if (col - 2) >= 0:
                black += yesterday[row, col - 2]
                black += yesterday[row - 1, col - 1]
            if (col + 2) < lobby.shape[1]:
                black += yesterday[row, col + 2]
                black += yesterday[row - 1, col + 1]
        if (row + 1) < lobby.shape[0]:
            if (col - 2) >= 0:
                black += yesterday[row + 1, col - 1]
            if (col + 2) < lobby.shape[1]:
                black += yesterday[row + 1, col + 1]

        if tile == BLACK:
            if black == 0 or black > 2:
                lobby[idx] = WHITE
        if tile == WHITE:
            if black == 2:
                lobby[idx] = BLACK

print(
    f"There are {np.count_nonzero(lobby)} tiles left with the black side up after {DAYS} days"
)
