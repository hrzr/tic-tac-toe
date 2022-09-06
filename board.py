from cell import Cell
from typing import Tuple
from errors import IsOccupied


class Board:
    """
    The class that represents a board of the tic-tac-toe game. It could be 3x3, 4x4 or 5x5.
    """

    def __init__(self, size: int = 3) -> None:
        """
        Inits the board with the desirable size.

        :param size: the size of the board, int, should be 3, 4 or 5, defaults to 3
        """
        if not isinstance(size, int):
            raise TypeError(f"size={size} should be int, it's {type(size)} instead")
        if size not in (3, 4, 5):
            raise ValueError(f"size={size} should be 3, 4 or 5")
        # self.board = [[Cell()] * size] * size
        self.size = size
        self.board = list()
        for y in range(self.size):
            self.board.append(list())
            for x in range(self.size):
                self.board[y].append(Cell())

    def __str__(self) -> str:
        """
        Represents the board graphically.

        :return: str
        """
        r = str()
        for y_count, y in enumerate(self.board):
            for x, contents in enumerate(y):
                if x == self.size - 1:
                    r += f" {contents}\n"
                else:
                    r += f" {contents} |"
            if y_count != self.size - 1:
                r += f"{'-' * (4 * self.size - 1)}\n"
        return r

    def __repr__(self) -> str:
        """
        Represents the board as a class string.

        :return: str
        """
        return f"{self.__class__.__name__}()"  # TODO: add something here later

    def get_cell(self, x: int, y: int) -> Cell:
        """
        Gets the contains of the cell at (x, y).

        :param x: int, [0, (self.size - 1)] X coordinate of the cell
        :param y: int, [0, (self.size - 1)] Y coordinate of the cell
        :return: Cell object
        """
        if not isinstance(x, int):
            raise TypeError(f"x={x} should be int, it's {type(x)} instead")
        if not (0 <= x < self.size):
            raise ValueError(f"x={x} should be from 0 to {self.size - 1}")
        if not isinstance(y, int):
            raise TypeError(f"x={y} should be int, it's {type(y)} instead")
        if not (0 <= y < self.size):
            raise ValueError(f"y={y} should be from 0 to {self.size - 1}")
        return self.board[y][x]

    def set_cell(self, coord: Tuple[int, int], fill_mark: str) -> None:
        """
        Sets a Cell at coord (should be valid coordinate) with fill_mark (should be valid fill mark)
        :param coord: tuple of x and y, that represent the space on the board
        :param fill_mark: str, 'X' or 'Y'
        :raises IsOccupied: if the Cell is not empty
        :return: None
        """
        if not isinstance(coord, tuple):
            raise TypeError(f"coord={coord} should be tuple, it's {type(coord)} instead")
        if not (0 <= coord[0] < self.size):
            raise ValueError(f"coord[0]={coord[0]} should be from 0 to {self.size - 1}")
        if not (0 <= coord[1] < self.size):
            raise ValueError(f"coord[1]={coord[1]} should be from 0 to {self.size - 1}")
        if fill_mark not in ('X', 'Y'):
            raise ValueError(f"fill_mark={fill_mark} should be either 'X' or 'Y'")
        if not self.board[coord[1]][coord[0]].is_occupied():
            self.board[coord[1]][coord[0]].occupy(fill_mark)
        else:
            raise IsOccupied(f"The Cell at {coord} is occupied with {self.board[coord[1]][coord[0]]}")

    def is_filled(self) -> bool:
        """
        Checks if the board is filled

        :return: True if every cell on the board is occupied, False if not
        """
        for y in self.board:
            for cell in y:
                if not cell.is_occupied():
                    return False
        return True

    def is_occupied(self, x: int, y: int) -> bool:
        """
        Checks if the cell at (x, y) is occupied.

        :param x: X coordinate, raises ValueError if it's out of range of [0, (self.size - 1)]
        :param y: Y coordinate, raises ValueError if it's out of range of [0, (self.size - 1)]
        :return: True if cell is occupied, False if it's not
        """
        if not (0 <= x < self.size):
            raise ValueError(f"x={x} should be from 0 to {self.size - 1}")
        if not (0 <= y < self.size):
            raise ValueError(f"y={y} should be from 0 to {self.size - 1}")
        return self.board[y][x].is_occupied()
