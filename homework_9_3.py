# Создать декоратор для функции, которая принимает список чисел. Декоратор должен производить предварительную проверку
# данных - удалять все четные элементы из списка.


from random import randint


def list_change_decorator(func_decorator):
    def remove_even_numbers(arguments):
        func_decorator(list(filter(lambda x: x % 2 == 1, arguments)))

    return remove_even_numbers


@list_change_decorator
def display_function(x):
    print(f'измененный список - {x}')


list_of_numbers = [randint(1, 999) for i in range(15)]

print(f'начальный список - {list_of_numbers}')
display_function(list_of_numbers)