# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).

dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
list_key = list(dict_1.keys())  # создаем список с ключами словаря dict_1
index = 0
while index <= len(list_key)-1:
    b = len(list_key[index])  # находим кол-во символов в элементах словаря по индексу
    dict_1[list_key[index] + str(b)] = dict_1.pop(list_key[index])  # добавляем в словарь новые ключи удаляя старые и возвращая их значение приcваиваем мх новым ключам
    index += 1
print(dict_1)

dict_2 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
list_key_2 = list(dict_2.keys())  # создаем список с ключами словаря dict_2
for i in range(len(list_key_2)):
    d = len(list_key_2[i])  # находим кол-во символов в элементах словаря по индексу
    dict_2[list_key_2[i] + str(d)] = dict_2.pop(list_key_2[i])   # добавляем в словарь новые ключи удаляя старые и возвращая их значение приcваиваем их новым ключам
print(dict_2)

