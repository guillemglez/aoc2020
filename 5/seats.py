from typing import Dict, Tuple

seats: Dict[int, bool] = {}
for sid in range(128 * 8):
    seats[sid] = False

with open('input') as f:
    for line in f:
        line = line.strip()

        step: Tuple[int, int] = (1 << 7, 1 << 3)
        row: Tuple[int, int] = (0, step[0])
        col: Tuple[int, int] = (0, step[1])
        for c in line:
            if c == 'F':
                step = (step[0] // 2, step[1])
                row = (row[0], row[1] - step[0])
            if c == 'B':
                step = (step[0] // 2, step[1])
                row = (row[0] + step[0], row[1])
            if c == 'L':
                step = (step[0], step[1] // 2)
                col = (col[0], col[1] - step[1])
            if c == 'R':
                step = (step[0], step[1] // 2)
                col = (col[0] + step[1], col[1])

        sid = row[0] * 8 + col[0]
        seats[sid] = True

front = True
for sid in range(128 * 8):
    occupied = seats[sid]
    if not occupied and front:
        continue
    if occupied and front:
        front = False
    if not occupied and not front:
        print(f"Your seat ID is {sid}!")
        break
