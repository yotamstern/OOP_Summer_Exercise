class Shape:
    """
    A class representing a generic shape with a color.

    Attributes:
    -----------
    color : str
        The color of the shape.

    Methods:
    --------
    set_color(color: str):
        Sets the color of the shape.

    get_color() -> str:
        Returns the color of the shape.
    """

    def __init__(self, color):
        """
        Initializes the Shape instance with a color.

        Parameters:
        -----------
        color : str
            The color of the shape. Must be a string.
        """
        # Assert that color is a string
        assert isinstance(color, str), "Color must be a string."
        self.color = color

    def set_color(self, color):
        """
        Sets the color of the shape.

        Parameters:
        -----------
        color : str
            The new color to set for the shape. Must be a string.
        """
        # Assert that color is a string before setting
        assert isinstance(color, str), "Color must be a string."
        self.color = color

    def get_color(self):
        """
        Returns the current color of the shape.

        Returns:
        --------
        str:
            The color of the shape.
        """
        return self.color
