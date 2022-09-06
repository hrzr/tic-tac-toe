from board import Board


class Player:
    """
    The class represents the Player, who could be the person, or a computer
    """

    def __init__(self, name: str, fill_mark: str, board: Board) -> None:
        """
        
        :param name:
        :param fill_mark:
        :param board:
        """
        self.name = name
        self.fill_mark = fill_mark
        self.board = board

    def make_move(self, x: int, y: int):
        if not self.board.is_occupied(x, y):
            self.board.set_cell((x, y), self.fill_mark)
        else:
            print("Эта клетка уже занята")

    def does_win(self):
        if all(cell.contents == self.fill_mark for cell in self.board[:3]) or \
                all(cell.contents == self.fill_mark for cell in self.board[3:6]) or \
                all(cell.contents == self.fill_mark for cell in self.board[6:]) or \
                all(cell.contents == self.fill_mark for cell in self.board[::3]) or \
                all(cell.contents == self.fill_mark for cell in self.board[1::3]) or \
                all(cell.contents == self.fill_mark for cell in self.board[2::3]) or \
                all(cell.contents == self.fill_mark for cell in self.board[::4]) or \
                all(cell.contents == self.fill_mark for cell in self.board[2:7:2]):
            return True
        else:
            return False
