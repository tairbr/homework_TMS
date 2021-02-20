x = int(input('Сколько будет гостей?:\n'))
if x >= 20 and x <= 50:
    print('Кафе')
elif x > 50:
    print('Ресторан')
else:
    print('Дома')