from board import Board
from player import Player
from computer import Computer
from errors import IsOccupied


def main():
    while True:
        try:
            board = Board(int(input("Choose the size of the board (3, 4, 5): ")))
            break
        except ValueError:
            print("The input should be int that equals to 3, 4 or 5")
    player1 = Player(name=input("Player 1, enter your name: "), fill_mark='X', board=board)
    if input("Do you want the second player to be the AI? (y/n) ").lower().startswith('y'):
        player2 = Computer(fill_mark='X', board=board)
    else:
        player2 = Player(name=input("Player 2, enter your name: "), fill_mark='O', board=board)
    is_player1 = True
    while not (board.is_filled() or player1.does_win() or player2.does_win()):
        player = player1 if is_player1 else player2
        print(board)
        print(f"player1.does_win(): {player1.does_win()}")
        print(f"player2.does_win(): {player2.does_win()}")
        while True:
            try:
                if not isinstance(player, Computer):
                    coordinates_str = input(f"{player.name}, please input the coordinates: ")
                    x, y = map(int, coordinates_str.strip('\n').split())
                    player.put(x, y)
                else:
                    player.put()
                is_player1 = not is_player1
                break
            except IsOccupied:
                print("That cell is already occupied. Try another one.")
            except ValueError as ve:
                print(f"The ValueError has occured: {str(ve)}")
    print(board)
    if player1.does_win():
        print(f"{player1.name} won")
    elif player2.does_win():
        print(f"{player2.name} won")
    else:
        print("Tie")


if __name__ == "__main__":
    main()
