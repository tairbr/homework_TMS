# 2. Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по умолчанию 0). Методы: увеличить
# скорости(скорость + 5), уменьшение скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
# разворот(изменение знака скорости). Все атрибуты приватные.

class Car:
    def __init__(self, brand, model, year_of_issue):
        self.__brand = brand
        self.__model = model
        self.__year_of_issue = year_of_issue
        self.__speed = 0

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def year_of_issue(self):
        return self.__year_of_issue

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    def up_speed(self):
        self.__speed = self.speed + 5

    def down_speed(self):
        self.__speed = self.speed - 5

    def stop(self):
        self.__speed = 0

    def print_speed(self):
        print(f'Speed - {self.__speed} km/h')

    def reversal(self):
        self.__speed = self.speed * -1


car_1 = Car('VW', 'Passat B6', 2007)

print(f'Марка: {car_1.brand}, модель - {car_1.model}, год выпуска - {car_1.year_of_issue}, - скорость {car_1.speed} км/ч')

car_1.up_speed()
car_1.up_speed()
car_1.up_speed()
print(f'Марка: {car_1.brand}, модель - {car_1.model}, год выпуска - {car_1.year_of_issue}, - скорость {car_1.speed} км/ч')
car_1.stop()
print(f'Марка: {car_1.brand}, модель - {car_1.model}, год выпуска - {car_1.year_of_issue}, - скорость {car_1.speed} км/ч')
car_1.up_speed()
car_1.up_speed()
car_1.print_speed()
car_1.reversal()
car_1.print_speed()
print(f'Марка: {car_1.brand}, модель - {car_1.model}, год выпуска - {car_1.year_of_issue}, - скорость {car_1.speed} км/ч')


