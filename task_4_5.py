# Составить список чисел Фибоначчи содержащий 15 элементов.


list_new = [1, 1]
index = 1
while index <= 13:
    a = list_new[index]
    b = list_new[index - 1]
    list_new.append(a + b)
    index += 1
print(list_new)

list_new_2 = [1, 1]
for i in range(1, 14):
    z = list_new_2[i]
    x = list_new_2[i - 1]
    list_new_2.append(z + x)
print(list_new_2)
