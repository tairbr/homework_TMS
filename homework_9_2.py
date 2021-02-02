# Создать lambda функцию, которая принимает на вход неопределенное количество именных аргументов и выводит словарь с
# ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}

func_1 = lambda **kwargs: {key*2: value for key, value in kwargs.items()}
print(func_1(abc=5, chi=8, k=43, rik=12))