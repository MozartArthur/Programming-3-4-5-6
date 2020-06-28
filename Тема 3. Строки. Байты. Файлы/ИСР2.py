#Создание скрипта для считывания данных справочных логов из текстового файла и преобразования их в CSV-формат с последующей записью в новый файл.

import csv

with open('MOCK_DATA.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('MOCK_DATA.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)