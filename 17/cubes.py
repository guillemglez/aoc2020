from typing import List, Tuple
import numpy as np

ACTIVE = '#'
INACTIVE = '.'
CYCLES = 6

with open('input') as f:
    inpt = f.read().strip()

cubesize = (len(inpt.split()) + 2 * CYCLES, ) * 3
cubes = np.full(cubesize, INACTIVE, dtype=str)

for iy, line in enumerate(inpt.split()):
    for ix, value in enumerate(line.strip()):
        if value == INACTIVE:
            continue
        x = cubesize[0] // 2 - len(inpt.split()) // 2 + ix
        y = cubesize[1] // 2 - len(inpt.split()) // 2 + iy
        z = cubesize[2] // 2
        cubes[x, y, z] = value

for cycle in range(CYCLES):
    previous = cubes.copy()
    for idx, value in np.ndenumerate(previous):
        # yapf: disable
        active = np.count_nonzero(previous[
            idx[0] - 1 if idx[0] - 1 >= 0 else 0: idx[0] + 2 if idx[0] + 2 < previous.shape[0] else previous.shape[0],
            idx[1] - 1 if idx[1] - 1 >= 0 else 0: idx[1] + 2 if idx[1] + 2 < previous.shape[1] else previous.shape[1],
            idx[2] - 1 if idx[2] - 1 >= 0 else 0: idx[2] + 2 if idx[2] + 2 < previous.shape[2] else previous.shape[2]
        ] == ACTIVE) - (1 if value == ACTIVE else 0)
        # yapf: enable

        if value == ACTIVE:
            if active != 2 and active != 3:
                cubes[idx] = INACTIVE

        if value == INACTIVE and active == 3:
            cubes[idx] = ACTIVE

print(f"There are {np.count_nonzero(cubes == ACTIVE)} cubes in active state")
