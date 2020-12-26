from typing import List, Dict, Tuple, Optional

from hexagon import Hexagon


def simplify(path: List[str]) -> List[str]:
    path = path.copy()

    while 'se' in path and 'ne' in path:
        path.remove('se')
        path.remove('ne')
        path.append('e')

    while 'sw' in path and 'nw' in path:
        path.remove('sw')
        path.remove('nw')
        path.append('w')

    while 'se' in path and 'w' in path:
        path.remove('se')
        path.remove('w')
        path.append('sw')

    while 'ne' in path and 'w' in path:
        path.remove('ne')
        path.remove('w')
        path.append('nw')

    while 'sw' in path and 'e' in path:
        path.remove('sw')
        path.remove('e')
        path.append('se')

    while 'nw' in path and 'e' in path:
        path.remove('nw')
        path.remove('e')
        path.append('nw')

    while 'e' in path and 'w' in path:
        path.remove('e')
        path.remove('w')

    while 'se' in path and 'nw' in path:
        path.remove('se')
        path.remove('nw')

    while 'ne' in path and 'sw' in path:
        path.remove('ne')
        path.remove('sw')

    while 'e' in path and 'w' in path:
        path.remove('e')
        path.remove('w')

    return path


central = Hexagon()

with open('test') as f:
    for line in f:
        last: Optional[str] = None
        path: List[str] = []
        for cardinal in line:
            if cardinal == 'n' or cardinal == 's':
                last = cardinal
                continue
            elif cardinal == 'e' or cardinal == 'w':
                if last:
                    cardinal = last + cardinal
                    last = None
                path.append(cardinal)

        current = central
        for direction in simplify(path):
            current = central.neighbor(direction)
            print(current.getIndex())
        current.flip()

        print(path)
        print(simplify(path))

cnt = 0
for tile in Hexagon.tiles:
    if tile.getColor() is Hexagon.BLACK:
        cnt += 1

print(cnt, len(Hexagon.tiles))
