# 4. Создать универсальный декоратор, который меняет порядок аргументов в функции на противоположный.

def universal_decorator_for_arguments(func_decorator):
    def to_change_the_order_of_arguments(*args):
        func_decorator(*args[::-1])
    return to_change_the_order_of_arguments


@universal_decorator_for_arguments
def func_x(*args):
    print(args)


func_x(1, 5, 7, 8, 3, 8)