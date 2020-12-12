import math

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

print(f"The Manhattan distance is {int(abs(ship['x']) + abs(ship['y']))}")
