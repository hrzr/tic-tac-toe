from player import Player
from board import Board
import random
from typing import Tuple, List


class Computer(Player):
    """
    The class describes basic AI for playing tic-tac-toe.
    """

    def __init__(self, fill_mark: str, board: Board) -> None:
        """
        Initialize the instance with super() of the Player class, but give a default name

        :param fill_mark: str, 'X' or 'O'
        :param board: Board, the board the players play on
        """
        super().__init__(name="DeepBlueTTT", fill_mark=fill_mark, board=board)
        # which stays for "DeepBlue Tic-Tac-Toe"

    @staticmethod
    def __check_win_on_any_board(board: Board, fill_mark: str) -> bool:
        """
        A method that checks any board with any fill_mark.

        :param board: Board, the board we are checking
        :param fill_mark: str, the fill mark we are checking
        :return:
        """
        for y in board.board:
            # if one of the all horizontal has same contents
            if all(cell.contents == fill_mark for cell in y):
                return True
        for x in range(board.size):
            # if one of the vertical has same contents
            if all(board.get_cell(x, y).contents == fill_mark for y in range(board.size)):
                return True
        if all(board.get_cell(i, i).contents == fill_mark for i in range(board.size)):
            # if top to bottom diagonal has same contents
            return True
        if all(board.get_cell(i, board.size - 1 - i).contents == fill_mark for i in range(board.size)):
            # if bottom to top diagonal has same contents
            return True
        return False

    def __get_dangerous_coords(self):  # do not know how to annotate that yet
        """
        Calculate coordinates of the points, that will instantly result in another player's winning.

        :return: Tuple[int, int] or Tuple[None, None] (if there are no dangerous points at the board)
        """
        another_mark = 'O' if self.fill_mark == 'X' else 'X'
        for y in range(self.board.size):
            for x in range(self.board.size):
                if not self.board.get_cell(x, y).is_occupied():
                    self.board.set_cell((x, y), another_mark)
                    if self.__check_win_on_any_board(self.board, another_mark):
                        self.board.board[y][x].contents = ' '
                        return x, y
                    else:
                        self.board.board[y][x].contents = ' '
        return None, None

    def __get_available(self) -> List[Tuple[int, int]]:
        """
        Gets all empty coordinates in a list of tuples.

        :return:
        """
        res = list()
        for y in range(self.board.size):
            for x in range(self.board.size):
                if not self.board.is_occupied(x, y):
                    res.append((x, y))
        return res

    def put(self, x=None, y=None) -> None:
        """
        The method that makes a move based on the algorythm.

        :param x: None, for compatibility, please don't use
        :param y: None, for compatibility, please don't use
        :return: None
        """
        if x is None and y is None:
            x, y = self.__get_dangerous_coords()
            if x is None and y is None:
                if not self.board.get_cell(self.board.size // 2, self.board.size // 2).is_occupied():
                    self.board.set_cell((self.board.size // 2, self.board.size // 2), self.fill_mark)
                else:
                    self.board.set_cell(random.choice(self.__get_available()), self.fill_mark)
            else:
                self.board.set_cell((x, y), self.fill_mark)
        else:
            raise ValueError(f"{x} and {y} should stay None")
