from player import Player
from board import Board
import random


class Computer(Player):
    """
    The class describes basic AI for playing tic-tac-toe.
    """

    def __init__(self, fill_mark: str, board: Board) -> None:
        super().__init__(name="DeepBlueTTT", fill_mark=fill_mark, board=board)
        # which stays for "DeepBlue Tic-Tac-Toe"

    @staticmethod
    def __check_win_on_any_board(board: Board, fill_mark: str) -> bool:
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

    def __get_dangerous_coords(self):
        choose_from = list()
        for y_counter, y in enumerate(self.board.board):
            for x_counter, x in enumerate(y):
                if self.board.get_cell(x, y).contents == ' ':
                    self.board.set_cell((x, y), self.fill_mark)
                    choose_from.append((x, y))
                    if self.__check_win_on_any_board(self.board, self.fill_mark):
                        self.board.set_cell((x, y), ' ')
                        return x, y
                    else:
                        self.board.set_cell((x, y), ' ')
        return None, None

    def put(self, x=None, y=None) -> None:
        """
        The method that makes a move based on the algorythm.

        :param x: None, for compatibility, please don't use
        :param y: None, for compatibility, please don't use
        :return: None
        """
        if x is None and y is None:
            if self.fill_mark == 'X':
                if not self.board.is_occupied(self.board.size // 2, self.board.size // 2):
                    self.board.set_cell((self.board.size // 2, self.board.size // 2), self.fill_mark)
                else:
                    pass
            else:
                pass
        else:
            raise ValueError(f"{x} and {y} should stay None")
