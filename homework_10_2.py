# Создать csv файл с данными о ежедневной погоде. Структура: Дата, Место, Градусы, Скорость ветра.
# Найти среднюю погоду(скорость ветра и градусы) для Минск за последние 7 дней.

import csv

with open("homework_10_2_1.csv", 'r') as csv_file:
    file_reader = csv.reader(csv_file, delimiter=",")
    headers = next(file_reader)
    average_temperature = 0
    average_wind_speed = 0

    for row in file_reader:
        average_temperature += int(row[2])
        average_wind_speed += int(row[3])
        town = row[1]

print(f'Средняя температура за 7 дней города {town}: {round(average_temperature / 7)} градусов')
print(f'Средняя скорость ветра - {round(average_wind_speed / 7)}м/с')
