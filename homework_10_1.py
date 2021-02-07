# Создать csv файл с данными следующей структуры: Имя, Фамилия, Возраст. Создать отчетный файл с информацией по
# количеству людей входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.

import csv

count = {'1-12': 0, '13-18': 0, '19-25': 0, '26-40': 0, '40+': 0}

with open("homework_10_1_1.csv", 'r') as csv_file:
    file_reader = csv.DictReader(csv_file, delimiter=",")
    for row in file_reader:
        if 1 < int(row[" Возраст"]) < 12:
            count['1-12'] = count['1-12'] + 1
        elif 13 < int(row[" Возраст"]) < 18:
            count['13-18'] = count['13-18'] + 1
        elif 19 < int(row[" Возраст"]) < 25:
            count['19-25'] = count['19-25'] + 1
        elif 26 < int(row[" Возраст"]) < 40:
            count['26-40'] = count['26-40'] + 1
        else:
            count['40+'] = count['40+'] + 1

with open("homework_10_1_2.csv", mode="w") as csv_file:
    names = ['1-12', '13-18', '19-25', '26-40', '40+']
    file_writer = csv.DictWriter(csv_file, delimiter=",", lineterminator="\r", fieldnames=names)
    file_writer.writeheader()
    file_writer.writerow(count)
