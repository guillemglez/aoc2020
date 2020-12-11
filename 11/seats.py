from typing import List

OCCUPIED = '#'
EMPTY = 'L'
FLOOR = '.'

seats: List[List[str]] = []
with open('input') as f:
    for line in f:
        seats.append([char for char in line.strip()])


def surrounding(seats: List[List[str]], row: int, col: int) -> int:
    occupied = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == j and j == 0:
                continue
            if row + i < 0 or row + i >= len(seats):
                continue
            if col + j < 0 or col + j >= len(seats[0]):
                continue

            occupied += 1 if seats[row + i][col + j] == OCCUPIED else 0
    return occupied


while True:
    nextround = [row.copy() for row in seats]
    occupied = 0
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seat == EMPTY and surrounding(seats, i, j) == 0:
                nextround[i][j] = OCCUPIED
            if seat == OCCUPIED:
                occupied += 1
                if surrounding(seats, i, j) >= 4:
                    nextround[i][j] = EMPTY

    if seats == nextround:
        break
    seats = nextround

print(f"There are {occupied} occupied seats looking at adjacent positions.")

seats = []
with open('input') as f:
    for line in f:
        seats.append([char for char in line.strip()])


def insight(seats: List[List[str]], row: int, col: int) -> int:
    occupied = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == j and j == 0:
                continue

            di = i
            dj = j
            while True:
                if row + di < 0 or row + di >= len(seats):
                    break
                if col + dj < 0 or col + dj >= len(seats[0]):
                    break
                if seats[row + di][col + dj] == OCCUPIED:
                    occupied += 1
                    break
                if seats[row + di][col + dj] == EMPTY:
                    break
                di += i
                dj += j

    return occupied


while True:
    nextround = [row.copy() for row in seats]
    occupied = 0
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seat == EMPTY and insight(seats, i, j) == 0:
                nextround[i][j] = OCCUPIED
            if seat == OCCUPIED:
                occupied += 1
                if insight(seats, i, j) >= 5:
                    nextround[i][j] = EMPTY

    if seats == nextround:
        break
    seats = nextround

print(f"There are {occupied} occupied seats when looking around.")
