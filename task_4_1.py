# Дан список целых чисел. Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2


list_1 = [1, 4, 5, 234, 6, 4, 345, 23, 98889]
list_new = []
index = 0
while index <= len(list_1)-1:
    list_new.append(list_1[index]*-2)
    index += 1
print(list_new)


list_2 = [1, 4, 5, 234, 6, 4, 345, 23, 98889]
list_new_2 = []
for i in range(len(list_2)):
    list_new_2.append(list_2[i]*-2)
print(list_new_2)
