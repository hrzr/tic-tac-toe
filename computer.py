from player import Player
from board import Board


class Computer(Player):
    """
    The class describes basic AI for playing tic-tac-toe.
    """

    def __init__(self, fill_mark: str, board: Board) -> None:
        super().__init__(name="DeepBlueTTT", fill_mark=fill_mark, board=board)

    def put(self, x=None, y=None) -> None:
        """
        The method that makes a move based on the algorythm.

        :param x: None, for compatibility, please don't use
        :param y: None, for compatibility, please don't use
        :return: None
        """
        if x is None and y is None:
            pass
        else:
            raise ValueError(f"{x} and {y} should stay None")
