from errors import IsOccupied


class Cell:
    """
    The class represents one cell of a board. A cell has
        - the number
        - it's contains: ' ', 'X' or 'O'  # probably should be str(number), 'X' or 'O'
    """
    number = 0

    def __init__(self) -> None:
        """
        Initialize an instance of a Cell. The number is generated automatically.
        """
        self.num = Cell.number
        Cell.number += 1
        self.contents = ' '  # is should be, i.e. str(num)

    def __str__(self) -> str:
        """
        Represents a Cell in a string form.

        :return: str(self.contents)
        """
        return str(self.contents)

    def __repr__(self) -> str:
        """
        Represents a Cell as a class string.

        :return: str, that contains ' ', 'X' or 'O'
        """
        return f"{self.__class__.__name__}(num={self.num}, contents='{self.contents}')"

    def is_occupied(self) -> bool:
        """
        Checks if the instance of the Cell contains something (i.e. 'X' or 'Y')

        :return: True if the contents either 'X' or 'Y', False if it's ' '
        """
        return self.contents != ' '

    def occupy(self, fill: str) -> None:
        """
        Occupies a cell with either 'X' or 'O'. Raises IsOccupied error if is already occupied.

        :param fill: str, 'X' or 'Y', raises ValueError if it's something else
        :return: None
        """
        if fill not in ('X', 'O', ' '):
            raise ValueError(f"fill={fill} should be either 'X', 'O' or ' '")
        if not self.is_occupied():
            self.contents = fill
        else:
            raise IsOccupied("The cell is not empty")
