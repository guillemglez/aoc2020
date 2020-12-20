from typing import List, Tuple, Dict
import numpy as np

BLACK = '#'
WHITE = '.'

with open('input') as f:
    inpt = f.read().strip()

tiles: Dict[int, np.ndarray] = {}
for rawtile in inpt.split('\n\n'):
    rows = rawtile.split('\n')
    tileid = int(rows.pop(0).split()[-1][:-1])  # "Tile XXXX:"
    tile = np.where(np.array([list(r) for r in rows]) == WHITE, 1, 0)
    tiles[tileid] = tile


# Convert border to an int ID (bit representation)
def bordertoint(pixels: np.ndarray) -> int:
    border = 0
    for i in range(len(pixels)):
        if pixels[i] > 0:
            border += (1 << i)
    return border


borders: Dict[int, List[int]] = {}
for tileid, tile in tiles.items():
    borders[tileid] = [
        bordertoint(tile[0, ...].flatten()),
        bordertoint(tile[..., -1].flatten()),
        bordertoint(tile[-1, ::-1].flatten()),
        bordertoint(tile[::-1, 0].flatten())
    ]

corners = 1
allborders = np.array([v for v in borders.values()]).flatten()
for tileid, bordercodes in borders.items():
    # Whether there is another equal border (the same border, but reversed, should also be looked into)
    other = [(np.count_nonzero(allborders == bordercode) + np.count_nonzero(
        allborders == int('{:010b}'.format(bordercode)[::-1], 2))) > 1
             for bordercode in bordercodes]
    # Find whether it is a corner
    if other in [[True, True, False, False], [False, True, True, False],
                 [False, False, True, True], [True, False, False, True]]:
        corners *= tileid

print(f"The four corner tiles multiplied give {corners}")
