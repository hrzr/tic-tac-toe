from board import Board
from player import Player
from computer import Computer


def main():
    board = Board()
    player1 = Player(name="Vasya", fill_mark='X', board=board)
    player2 = Player(name="Petya", fill_mark='Y', board=board)
    is_player1 = True
    while not board.is_occupied() or player1.does_win() or player2.does_win():
        player_x = input("Input the coordinates: ")


if __name__ == "__main__":
    main()