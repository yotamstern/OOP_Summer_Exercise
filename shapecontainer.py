import random
from square import Square
from rectangle import Rectangle
from circle import Circle


LIST_OF_COLORS = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'black', 'white', 'gray']


class ShapeContainer:
    """
    A class that holds and manages a collection of various shapes (Square, Rectangle, Circle).

    Attributes:
    -----------
    list_of_shapes : list
        A list that stores different shape objects (Square, Rectangle, Circle).

    Methods:
    --------
    generate(num: int):
        Generates random shapes and adds them to the list.

    sum_area() -> float:
        Returns the total area of all the shapes in the list.

    sum_perimeter() -> float:
        Returns the total perimeter of all the shapes in the list.

    count_colors() -> dict:
        Returns a dictionary that counts how many shapes have each color.
    """

    def __init__(self):
        """
        Initializes an empty list to store shape objects.
        """
        self.list_of_shapes = []

    def generate(self, num):
        """
        Generates random shapes (Square, Rectangle, or Circle) with random sizes and colors,
        then adds them to the list.

        Parameters:
        -----------
        num : int
            The number of shapes to generate.
        """
        for i in range(num):
            shape_type = random.randint(1, 3)
            color = random.choice(LIST_OF_COLORS)

            if shape_type == 1:
                new_shape = Square(color, random.randint(1, 10))
            elif shape_type == 2:
                new_shape = Rectangle(color, random.randint(1, 10),
                                      random.randint(1, 10))
            else:
                new_shape = Circle(color, random.randint(1, 10))

            self.list_of_shapes.append(new_shape)

    def sum_area(self):
        """
        Calculates the total area of all the shapes in the list.

        Returns:
        --------
        float:
            The sum of the areas of all shapes.
        """
        area = 0
        for shape in self.list_of_shapes:
            area += shape.get_area()
        return area

    def sum_perimeter(self):
        """
        Calculates the total perimeter of all the shapes in the list.

        Returns:
        --------
        float:
            The sum of the perimeters of all shapes.
        """
        perimeter = 0
        for shape in self.list_of_shapes:
            perimeter += shape.get_perimeter()
        return perimeter

    def count_colors(self):
        """
        Counts how many shapes have each color from the list of shapes.

        Returns:
        --------
        dict:
            A dictionary where the keys are color names and the values are the count of shapes with that color.
        """
        dict_of_colors = {color: 0 for color in LIST_OF_COLORS}
        for shape in self.list_of_shapes:
            color = shape.get_color()

            if color in dict_of_colors:
                dict_of_colors[color] += 1
            else:
                dict_of_colors[color] = 1
        return dict_of_colors
