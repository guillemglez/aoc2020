import numpy as np


class Tile:
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

    VERTICAL = 0
    HORIZONTAL = 1

    def __init__(self, tileid: int, image: np.ndarray):
        self.id = tileid
        # TOP->0
        # RIGHT->1
        # BOTTOM->2
        # LEFT->3
        self.borders = [
            self.bordertoint(image[0, :].flatten()),
            self.bordertoint(image[:, -1].flatten()),
            self.bordertoint(image[-1, ::-1].flatten()),
            self.bordertoint(image[::-1, 0].flatten())
        ]
        self.image = image[1:-1, 1:-1]

    def bordertoint(self, pixels: np.ndarray) -> int:
        """Convert border to an int ID (bit representation)"""
        border = 0
        for i in range(len(pixels)):
            if pixels[i] > 0:
                border += (1 << i)
        return border

    def invertborder(self, border: int) -> int:
        return int('{:010b}'.format(border)[::-1], 2)

    def rotate(self) -> None:
        self.borders = [
            self.getborder(self.LEFT),
            self.getborder(self.TOP),
            self.getborder(self.RIGHT),
            self.getborder(self.BOTTOM)
        ]
        self.image = np.rot90(self.image, k=3)

    def getborder(self, border: int, candidate: bool = False) -> int:
        """
        Return border:
            TOP->0
            RIGHT->1
            BOTTOM->2
            LEFT->3
        """
        assert border in range(len(self.borders))
        if candidate:
            return self.invertborder(
                self.getborder(border=border, candidate=False))
        return self.borders[border]

    def flip(self, axis: int) -> None:
        """
        Flip tile:
            VERTICALLY->0
            HORIZONTALLY->1
        """
        assert axis in range(2)
        if axis == self.VERTICAL:
            self.borders = [
                self.invertborder(self.getborder(self.BOTTOM)),
                self.invertborder(self.getborder(self.RIGHT)),
                self.invertborder(self.getborder(self.TOP)),
                self.invertborder(self.getborder(self.LEFT))
            ]
            self.image = np.flipud(self.image)
        else:  # self.HORIZONTAL
            self.borders = [
                self.invertborder(self.getborder(self.TOP)),
                self.invertborder(self.getborder(self.LEFT)),
                self.invertborder(self.getborder(self.BOTTOM)),
                self.invertborder(self.getborder(self.RIGHT))
            ]
            self.image = np.fliplr(self.image)

    def fitsin(self, canvas, row, col):
        checked_tiles = 0  # If no tiles around this position, then it is not declared as fitting
        if (row - 1) >= 0:
            if canvas[row - 1, col] != 0:
                if canvas[row - 1, col].getborder(
                        self.BOTTOM, candidate=True) != self.getborder(
                            self.TOP):
                    return False
                else:
                    checked_tiles += 1
        if (row + 1) < canvas.shape[0]:
            if canvas[row + 1, col] != 0:
                if canvas[row + 1, col].getborder(
                        self.TOP, candidate=True) != self.getborder(
                            self.BOTTOM):
                    return False
                else:
                    checked_tiles += 1
        if (col - 1) >= 0:
            if canvas[row, col - 1] != 0:
                if canvas[row, col - 1].getborder(
                        self.RIGHT, candidate=True) != self.getborder(
                            self.LEFT):
                    return False
                else:
                    checked_tiles += 1
        if (col + 1) < canvas.shape[1]:
            if canvas[row, col + 1] != 0:
                if canvas[row, col + 1].getborder(
                        self.LEFT, candidate=True) != self.getborder(
                            self.RIGHT):
                    return False
                else:
                    checked_tiles += 1
        return checked_tiles > 0  # Prevents it to be placed in an empty place

    # For pretty-printing the canvas
    def __repr__(self):
        return f"T{self.id}"
