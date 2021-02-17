# Выполнить задание 1 с использованием класса Math. Класс принимает в качестве аргументов два числа. Определить 4 метода
# (сложение, вычитание, умножение, деление). Добавить валидацию входных данных. Программа должна состоять из четырех
# файлов(main.py, classes.py, ui_func.py exceptions.py)

from classes import Math
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
                resault = Math(number_1, number_2)
                print(f'Результат: {resault.addition()}')
            elif data_list[index_mathematical_operator] == '-':
                resault = Math(number_1, number_2)
                print(f'Результат: {resault.subtraction()}')
            elif data_list[index_mathematical_operator] == '*':
                resault = Math(number_1, number_2)
                print(f'Результат: {resault.multiplication()}')
            elif data_list[index_mathematical_operator] == '/':
                resault = Math(number_1, number_2)
                print(f'Результат: {resault.division()}')

        except ZeroDivisionError as err:
            print(f'На 0 делить нельзя!!!')
        except ValueError as err:
            print(f'Только числа!!!')