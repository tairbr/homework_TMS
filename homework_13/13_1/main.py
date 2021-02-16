# 1. Написать калькулятор. Программа должна содержать 4 функции принимающие два аргумента и возвращающие результаты
# сложения, вычитания, умножения и деления. Реализовать пользовательский интерфейс с бесконечным циклом.  Добавить
# валидацию входных данных. Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py, exceptions.py)

from func import addition, subtraction, multiplication, division
from exceptions import Layout_error

print('Калькулятор может: +, -, *, /. Вводи выражение в виде например: a+b. Для выхода набери - exit')

while True:
    try:
        input_user = input(':')
        if input_user == 'учше':
            raise Layout_error
    except Layout_error as err:
        print(err)

    if input_user == 'exit':
        break
    else:
        data_list = list(input_user)  # список с данными которые ввел пользователь
        mathematical_operator = []  # определяем математический оператор который ввел пользователь
        if '+' in data_list:
            mathematical_operator.append('+')
        elif '-' in data_list:
            mathematical_operator.append('-')
        elif '*' in data_list:
            mathematical_operator.append('*')
        else:
            mathematical_operator.append('/')

        try:

            index_mathematical_operator = data_list.index(
                mathematical_operator[0])  # индекс мат.оператора в списке data_list
            number_1 = float(input_user[0:index_mathematical_operator])  # определяем первое число
            number_2 = float(input_user[index_mathematical_operator + 1:])  # определяем второе число



            if data_list[index_mathematical_operator] == '+':
                print(f'Результат: {addition(number_1, number_2)}')
            elif data_list[index_mathematical_operator] == '-':
                print(f'Результат: {subtraction(number_1, number_2)}')
            elif data_list[index_mathematical_operator] == '*':
                print(f'Результат: {multiplication(number_1, number_2)}')
            elif data_list[index_mathematical_operator] == '/':
                print(f'Результат: {division(number_1, number_2)}')
        except ZeroDivisionError as err:
            print(f'На 0 делить нельзя!!!')
        except ValueError as err:
            print(f'Только числа!!!')

# a = int(input('a: '))
# b = int(input('b: '))
# try:
# result = a / b
# except ZeroDivisionError as err:
# print(f'b is zero - {err}!!!')
# except Exception as err:
# print(f'SOMETHING WRONG - {err}!!!')
# else:
# print('Ошибки не было' )
# finally:
# print('Сработает всегда' )

# class MyErr(Exception):
#     def __init__(self, mess='Zero cost'):
#         super().__init__(mess)
#
#
# class Book:
#     def __init__(self, pages, year, author, cost):
#         try:
#             self.pages = pages
#             self.year = year
#             self.author = author
#             self.cost = cost
#             if type(pages) != int:
#                 raise TypeError('Pages is not int')
#             if type(year) != int:
#                 raise TypeError('Year is not int')
#             if type(author) != str:
#                 raise TypeError('Author is not str')
#             if type(cost) != int:
#                 raise TypeError('Cost is not int')
#             if year > 2021:
#                 raise ValueError('Error year')
#
#             if cost == 0:
#                 raise MyErr
#
#         except TypeError as te:
#             print(te)
#
#         except ValueError as ve:
#             print(ve)
#
#         except MyErr as err:
#             print(f'cost is not valid - {err}')
#         else:
#             print('Data is correct')
#
#
# a = Book('str', 2022, 'Author', 10)
# b = Book(12, 'str', 'author', 10)
# c = Book(12, 2000, 45, 10)
# d = Book(12, 200, 'author', [])
# e = Book(12, 3000, 'author', 10)
# f = Book(12, 2000, 'author', 0)
