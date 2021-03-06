import math

## PART 1
with open('input') as f:
    ship = {'x': 0., 'y': 0., 'd': 0}
    for line in f:
        instruction = line[0]
        argument = int(line.strip()[1:])

        if instruction == 'E':
            ship['x'] += argument
        if instruction == 'N':
            ship['y'] += argument
        if instruction == 'W':
            ship['x'] -= argument
        if instruction == 'S':
            ship['y'] -= argument
        if instruction == 'L':
            ship['d'] += argument
        if instruction == 'R':
            ship['d'] -= argument

        if instruction == 'F':
            ship['x'] += math.cos(math.radians(ship['d'])) * argument
            ship['y'] += math.sin(math.radians(ship['d'])) * argument

print(f"The Manhattan distance is {round(abs(ship['x']) + abs(ship['y']))}")

## PART 2
with open('input') as f:
    ship = {'x': 0., 'y': 0., 'dx': 10, 'dy': 1}
    for line in f:
        instruction = line[0]
        argument = int(line.strip()[1:])

        if instruction == 'E':
            ship['dx'] += argument
        if instruction == 'N':
            ship['dy'] += argument
        if instruction == 'W':
            ship['dx'] -= argument
        if instruction == 'S':
            ship['dy'] -= argument

        if instruction == 'F':
            ship['x'] += ship['dx'] * argument
            ship['y'] += ship['dy'] * argument

        # https://en.wikipedia.org/wiki/Rotation_matrix#In_two_dimensions
        if instruction == 'L' or instruction == 'R':
            if instruction == 'R':
                argument *= -1
            x = ship['dx']
            ship['dx'] = x * math.cos(math.radians(
                argument)) - ship['dy'] * math.sin(math.radians(argument))
            ship['dy'] = x * math.sin(math.radians(
                argument)) + ship['dy'] * math.cos(math.radians(argument))

print(
    f"The corrected Manhattan distance is {round(abs(ship['x']) + abs(ship['y']))}"
)
