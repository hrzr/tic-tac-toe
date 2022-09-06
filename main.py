from board import Board
from player import Player
from computer import Computer


def main():
    board = Board()
    print(board)
    board
    print(board.get_cell(0, 0))


if __name__ == "__main__":
    main()