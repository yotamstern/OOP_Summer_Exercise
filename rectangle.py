from shape import Shape
from square import Square


class Rectangle(Shape):
    """
    A class representing a rectangle, which is a subclass of the Shape class.

    Attributes:
    -----------
    color : str
        The color of the rectangle (inherited from Shape).
    length : float
        The length of the rectangle.
    width : float
        The width of the rectangle.

    Methods:
    --------
    get_area() -> float:
        Returns the area of the rectangle.

    get_perimeter() -> float:
        Returns the perimeter of the rectangle.

    connect_rectangles(other: Rectangle) -> Rectangle:
        Combines the current rectangle with another rectangle to create a new rectangle
        with combined length and width.

    connect_rectangle_with_square(other: Square) -> Rectangle:
        Combines the current rectangle with a square to create a new rectangle
        with length and width increased by the side length of the square.
    """

    def __init__(self, color, length, width):
        """
        Initializes the Rectangle instance with a color, length, and width.

        Parameters:
        -----------
        color : str
            The color of the rectangle (passed to the parent class).
        length : float
            The length of the rectangle. Must be a positive number.
        width : float
            The width of the rectangle. Must be a positive number.
        """
        # Assert that length and width are positive numbers
        assert isinstance(length, (int, float)), "Length must be a number."
        assert length > 0, "Length must be greater than zero."
        assert isinstance(width, (int, float)), "Width must be a number."
        assert width > 0, "Width must be greater than zero."

        super().__init__(color)
        self.length = length
        self.width = width

    def get_area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        --------
        float:
            The area of the rectangle, which is length * width.
        """
        return self.length * self.width

    def get_perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
        --------
        float:
            The perimeter of the rectangle, which is 2 * length + 2 * width.
        """
        return 2 * self.length + 2 * self.width

    def connect_rectangles(self, other):
        """
        Combines the current rectangle with another rectangle by adding their lengths and widths.

        Parameters:
        -----------
        other : Rectangle
            Another rectangle to combine with the current rectangle.

        Returns:
        --------
        Rectangle:
            A new Rectangle instance with combined length and width.

        Raises:
        -------
        AssertionError:
            If the other object is not an instance of Rectangle.
        """
        # Assert that the other object is an instance of Rectangle
        assert isinstance(other, Rectangle), "Other must be an instance of Rectangle."

        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(self.color, new_length, new_width)

    def connect_rectangle_with_square(self, other):
        """
        Combines the current rectangle with a square by adding the square's side length
        to both the length and width of the rectangle.

        Parameters:
        -----------
        other : Square
            A square to combine with the current rectangle.

        Returns:
        --------
        Rectangle:
            A new Rectangle instance with the length and width increased by the side of the square.

        Raises:
        -------
        AssertionError:
            If the other object is not an instance of Square.
        """
        # Assert that the other object is an instance of Square
        assert isinstance(other, Square), "Other must be an instance of Square."

        new_length = self.length + other.side
        new_width = self.width + other.side
        return Rectangle(self.color, new_length, new_width)
