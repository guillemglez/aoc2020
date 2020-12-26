from typing import List, Dict, Tuple, TypeVar

HexagonType = TypeVar('HexagonType', bound='Parent')

class Hexagon:
    tiles: List[HexagonType] = []

    BLACK = 0
    WHITE = 1

    E = 'e'
    W = 'w'
    SE = 'se'
    SW = 'sw'
    NE = 'ne'
    NW = 'nw'

    def __init__(self):
        self.index = len(Hexagon.tiles)
        Hexagon.tiles.append(self)
        print(self.index)

        self.color = Hexagon.WHITE
        self.neighbors: Dict[str, Hexagon] = {}

    def neighbor(self, direction: str, propagate=True) -> HexagonType:
        if direction in self.neighbors.keys():
            print(f"Found {direction} at {self.index}")
            return self.neighbors[direction]
        else:
            return self.createat(direction, propagate)

    def createat(self, direction: str, propagate) -> HexagonType:
        self.neighbors[direction] = Hexagon()

        if propagate:
            nc, sc = self.getCollindants(direction)
            nnc, nsc = self.getCollindants(self.invertDirection(direction))

            self.neighbor(direction).neighborhood(nnc, self.neighbor(nc, False))
            self.neighbor(direction).neighborhood(nsc, self.neighbor(sc, False))

            self.neighbor(nc, False).neighborhood(self.invertDirection(nnc),
                                        self.neighbor(direction))
            self.neighbor(sc, False).neighborhood(self.invertDirection(nsc),
                                        self.neighbor(direction))

        return self.neighbors[direction]

    def neighborhood(self, direction: str, neighbor: HexagonType):
        self.neighbors[direction] = neighbor

    def flip(self):
        print(f"flip {self.index}")
        self.color = Hexagon.WHITE if self.getColor(
        ) is Hexagon.BLACK else Hexagon.BLACK

    def getColor(self) -> int:
        return self.color

    def getIndex(self) -> int:
        return self.color

    @staticmethod
    def invertDirection(direction: str) -> str:
        if direction == Hexagon.E:
            return Hexagon.W
        if direction == Hexagon.W:
            return Hexagon.E
        if direction == Hexagon.SW:
            return Hexagon.NE
        if direction == Hexagon.NW:
            return Hexagon.SE
        if direction == Hexagon.SE:
            return Hexagon.NW
        if direction == Hexagon.NE:
            return Hexagon.SW
        raise Exception(f"Inverting wrong direction {direction}?")

    @staticmethod
    def getCollindants(direction: str) -> Tuple[str, str]:
        if direction == Hexagon.E:
            return Hexagon.NE, Hexagon.SE
        if direction == Hexagon.W:
            return Hexagon.NW, Hexagon.SW
        if direction == Hexagon.SW:
            return Hexagon.W, Hexagon.SE
        if direction == Hexagon.NW:
            return Hexagon.NE, Hexagon.W
        if direction == Hexagon.SE:
            return Hexagon.E, Hexagon.SW
        if direction == Hexagon.NE:
            return Hexagon.NW, Hexagon.E
        raise Exception(f"Collindants for wrong direction {direction}?")
