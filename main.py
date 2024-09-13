from square import Square
from rectangle import Rectangle
from shapecontainer import ShapeContainer

s1 = Square('red', 5)
s2 = Square('blue', 8)
s3 = s1.connect_squares(s2)
r1 = Rectangle('white', 4, 5)
r2 = r1.connect_rectangle_with_square(s3)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.get_color())
my_container = ShapeContainer()
my_container.generate(100)
print("total area:", my_container.sum_area())
print("total perimeter:", my_container.sum_perimeter())
print("colors:", my_container.count_colors())