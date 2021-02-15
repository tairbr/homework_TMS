from math import pi
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point(x={}, y={})'.format(self.x, self.y)

class Figure:
    pass


class Circle(Figure):
    def __init__(self, centr, r):
        self.r = r
        self.centr = centr

    def perimeter(self):  # метод возвращает периметр
        return f'Perimeter circle: {2 * pi * self.r}'

    def area(self):  # метод возвращает площадь
        return f'Area circle: {pi * self.r ** 2}'


class Triangle(Figure):

    def __init__(self, vertex_1, vertex_2, vertex_3):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.vertex_3 = vertex_3
        self.len_side()

    def len_side(self):  # метод вычисления длинн сторон

        def gipotenuza(arg_1, arg_2):
            return sqrt((arg_1[0] - arg_2[0]) ** 2 + (arg_1[1] - arg_2[1]) ** 2)

        self.side_ab = gipotenuza((self.vertex_1.x, self.vertex_1.y), (self.vertex_2.x, self.vertex_2.y))
        self.side_bc = gipotenuza((self.vertex_2.x, self.vertex_2.y), (self.vertex_3.x, self.vertex_3.y))
        self.side_ca = gipotenuza((self.vertex_3.x, self.vertex_3.y), (self.vertex_1.x, self.vertex_1.y))

    def perimeter(self):  # метод возвращает периметр
        return f'Perimeter triangle: {(self.side_ab + self.side_bc + self.side_ca)}'

    def area(self):  # метод возвращает площадь
        semi_perimeter = (self.side_ab + self.side_bc + self.side_ca) / 2
        return f'Area triangle: {sqrt(semi_perimeter * (semi_perimeter - self.side_ab) * (semi_perimeter - self.side_bc) * (semi_perimeter - self.side_ca))}'


class Square(Figure):

    def __init__(self, vertex_1, vertex_2):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.len_side()

    def len_side(self):  # метод вычисления длинн сторон прямоугольника
        self.side_ab = self.vertex_2.y - self.vertex_1.y
        self.side_bc = self.vertex_2.x - self.vertex_1.x
        self.side_cd = self.side_ab
        self.side_da = self.side_bc
        return self.side_ab, self.side_bc, self.side_cd, self.side_da

    def perimeter(self):  # метод возвращает периметр
        return f'Perimeter square: {(self.side_ab + self.side_bc) * 2}'

    def area(self):  # метод возвращает площадь
        return f'Area square: {self.side_ab * self.side_bc}'