
from classes import Point, Circle, Triangle, Square


point_1 = Point(40, 65)
point_2 = Point(80, 134)
point_3 = Point(156, 21)
circule = Circle(point_1, 12)
triangle = Triangle(point_1, point_2, point_3)
square = Square(point_1, point_2)
list_figure = [circule, triangle, square]
for i in list_figure:
    print(i.area())
    print(i.perimeter())
