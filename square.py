from shape import Shape


class Square(Shape):
    """
    Attributes:
    -----------
    color : str
        The color of the square (inherited from Shape).
    side : float
        The length of one side of the square.

    Methods:
    --------
    get_area() -> float:
        Returns the area of the square.

    get_perimeter() -> float:
        Returns the perimeter of the square.

    connect_squares(other: Square) -> Square:
        Combines the current square with another square to create a new square
        with a side length equal to the sum of both squares' sides.
    """

    def __init__(self, color, side):
        """
        Initializes the Square instance with a color and side length.

        Parameters:
        -----------
        color : str
            The color of the square (passed to the parent class).
        side : float
            The length of one side of the square. Must be a positive number.
        """
        assert isinstance(side, (int, float)), "Side must be a number."
        assert side > 0, "Side must be greater than zero."

        super().__init__(color)
        self.side = side

    def get_area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        --------
        float:
            The area of the square, which is side * side.
        """
        return self.side * self.side

    def get_perimeter(self):
        """
        Calculates and returns the perimeter of the square.

        Returns:
        --------
        float:
            The perimeter of the square, which is 4 * side.
        """
        return 4 * self.side

    def connect_squares(self, other):
        """
        Combines the current square with another square by adding their side lengths.

        Parameters:
        -----------
        other : Square
            Another square to combine with the current square.

        Returns:
        --------
        Square:
            A new Square instance with a side length equal to the sum of both squares' sides.

        Raises:
        -------
        AssertionError:
            If the other object is not an instance of Square.
        """

        assert isinstance(other, Square), "Other must be an instance of Square."

        new_side = self.side + other.side
        return Square(self.color, new_side)
