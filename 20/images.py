from typing import List, Tuple, Dict
import numpy as np
import math

from tile import Tile

BLACK = '#'
WHITE = '.'

with open('input') as f:
    inpt = f.read().strip()

# Parse input to get the tiles, store them in the "bag"
# Store all the borders in a list to check them later
bag: Dict[int, Tile] = {}
borders: List[int] = []
for rawtile in inpt.split('\n\n'):
    rows = rawtile.split('\n')
    tileid = int(rows.pop(0).split()[-1][:-1])  # "Tile XXXX:"
    tile = np.where(np.array([list(r) for r in rows]) == WHITE, 1, 0)
    bag[tileid] = Tile(tileid, tile)
    for b in range(4):
        borders.append(bag[tileid].getborder(b))
        borders.append(bag[tileid].getborder(b, True))

# Look for a corner tile: only two borders of it match other pieces'
for cornertile in bag.values():
    invalid = []
    for b in range(4):
        invalid.append(borders.count(cornertile.getborder(b, True)) == 1)
    if invalid.count(True) == 2:
        break

# Correctly orientate the corner tile
while not invalid == [True, False, False, True]:
    cornertile.rotate()
    invalid = []
    for b in range(4):
        invalid.append(borders.count(cornertile.getborder(b, True)) == 1)

# Create a square canvas and place the corner tile
canvas: np.ndarray = np.zeros((int(math.sqrt(len(bag))), ) * 2, dtype=object)
canvas[0, 0] = bag.pop(cornertile.id)

# Place the tiles where they fit in the canvas
while len(bag):
    # Check each tile still in the bag
    for tile in bag.copy().values():
        # Flip it in both axis
        for flip in range(2):
            # Rotate it 90, 180 and 270 degrees clockwise
            for _ in range(3):
                for idx in np.ndindex(canvas.shape):
                    if canvas[idx] == 0 and tile.fitsin(canvas, *idx):
                        canvas[idx] = bag.pop(tile.id)
                        break
                if tile.id not in bag.keys():
                    break
                else:
                    tile.rotate()
            if tile.id not in bag.keys():
                break
            else:
                tile.flip(flip)

print(
    f"The four corner tiles multiplied give {canvas[0,0].id * canvas[0,-1].id * canvas[-1,0].id * canvas[-1,-1].id}"
)
