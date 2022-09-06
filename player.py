from board import Board
from errors import IsOccupied


class Player:
    """
    The class represents the Player, who could be the person, or a computer
    """

    def __init__(self, name: str, fill_mark: str, board: Board) -> None:
        """
        Initializes an new instance of Player with name, fill_mark and board

        :param name: str
        :param fill_mark: str, 'X' or 'Y'
        :param board: Board, represents a tic-tac-toe board
        """
        if not isinstance(name, str):
            raise TypeError(f"name={name} should be str, it's {type(name)} instead")
        if not isinstance(fill_mark, str):
            raise TypeError(f"fill_mark={fill_mark} should be str, it's {type(fill_mark)} instead")
        if fill_mark not in ('X', 'Y'):
            raise ValueError(f"fill_mark={fill_mark}, it should be either 'X' or 'Y'")
        if not isinstance(board, Board):
            raise TypeError(f"board={board} should be Board, it's {type(board)} instead")
        self.name = name
        self.fill_mark = fill_mark
        self.board = board

    def put(self, x: int, y: int) -> None:
        """
        Sets a cell at (x, y) with self.fill_mark.

        :param x: int, [0, (self.board.size - 1)]
        :param y: int, [0, (self.board.size - 1)]
        :raises IsOccupied: if the cell is already occupied
        :return: None
        """
        if not isinstance(x, int):
            raise TypeError(f"x={x} should be int, it's {type(x)} instead")
        if not (0 <= x < self.board.size):
            raise ValueError(f"x={x} should be from 0 to {self.board.size - 1}")
        if not isinstance(y, int):
            raise TypeError(f"x={y} should be int, it's {type(y)} instead")
        if not (0 <= y < self.board.size):
            raise ValueError(f"y={y} should be from 0 to {self.board.size - 1}")
        if not self.board.is_occupied(x, y):
            self.board.set_cell((x, y), self.fill_mark)
        else:
            raise IsOccupied(f"The Cell at ({x}, {y}) is occupied with {self.board.get_cell(x, y)}")

    def does_win(self) -> bool:
        """
        Returns if that player wins.

        :return: bool, stat of winning at the moment
        """
        for y in self.board.board:
            # if one of the all horizontal has same contents
            if all(cell.contents == self.fill_mark for cell in y):
                return True
        for x in range(self.board.size):
            # if one of the vertical has same contents
            if all(self.board.board[y][x] == self.fill_mark for y in range(self.board.size)):
                return True
        if all(self.board.get_cell(i, i) == self.fill_mark for i in range(self.board.size)):
            # if top to bottom diagonal has same contents
            return True
        if all(self.board.get_cell(i, (self.board.size - 1) - i) == self.fill_mark for i in range(self.board.size)):
            # if bottom to top diagonal has same contents
            return True
        return False
