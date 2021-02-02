# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i это порядковый номер строки в списке.
# Использовать генератор списков.

list_str = ('Dima', 'Kirill', 'Anton', 'Artem', 'Nikita', 'Jora')
list_new = [str(index + 1) + ' - ' + value for index, value in enumerate(list_str)]
print(list_new)
