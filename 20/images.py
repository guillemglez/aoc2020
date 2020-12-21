from typing import List, Tuple, Dict
import numpy as np
import math

from tile import Tile

BLACK = '#'
WHITE = '.'

MONSTER = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

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

desert = np.zeros(tuple([x * 8 for x in canvas.shape]), dtype=np.uint8)
for idx, tile in np.ndenumerate(canvas):
    row, col = idx
    desert[row * 8:(row + 1) * 8,
           col * 8:(col + 1) * 8] = tile.image.astype(np.uint8)

# Parse MONSTER input
monster = np.zeros((len(MONSTER.split('\n')), len(MONSTER.split('\n')[0])),
                   dtype=np.uint8)
for row, line in enumerate(MONSTER.split('\n')):
    for col, char in enumerate(list(line)):
        if char != BLACK:
            monster[row, col] = 1

# Look for monsters
rough = np.count_nonzero(desert == 0)
# Flip desert in both axis
for flip in range(2):
    # Rotate desert 90, 180 and 270 degrees (anticlockwise)
    for _ in range(3):
        for idx in np.ndindex(desert.shape):
            row, col = idx
            if row + monster.shape[0] >= desert.shape[0]:
                continue
            if col + monster.shape[1] >= desert.shape[1]:
                continue
            if np.all(desert[row:row + monster.shape[0],
                             col:col + monster.shape[1]][monster == 0] == 0):
                rough -= np.count_nonzero(monster == 0)
        desert = np.rot90(desert)
    if flip == Tile.VERTICAL:
        desert = np.flipud(desert)
    if flip == Tile.HORIZONTAL:
        desert = np.fliplr(desert)

print(
    f"The four corner tiles multiplied give {canvas[0,0].id * canvas[0,-1].id * canvas[-1,0].id * canvas[-1,-1].id}"
)
print(f"The waters are rough by {rough}")
