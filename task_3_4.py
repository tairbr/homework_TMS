x = input('Введи строку:\n')
z = len(x)
if z % 2 == 0:
    print('Добавь еще один символ!')
else:
    if x[int(z/2)] == x[0]:
        print(x[1:-1])
    else:
        print(x[int(z/2)])