# Дан список целых чисел. Подсчитать сколько четных чисел в списке

list_1 = [45, 6, 32, 456, 2, 8, 56, 975467, 34526]
index = 0
a = 0
while index <= len(list_1)-1:
    if list_1[index] % 2 == 0:
        a += 1
        index += 1
    else:
        index += 1
print(a)

list_2 = [45, 6, 32, 456, 2, 8, 56, 975467, 34526]
b = 0
for i in range(len(list_2)):
    if list_2[i] % 2 == 0:
        b += 1
print(b)
