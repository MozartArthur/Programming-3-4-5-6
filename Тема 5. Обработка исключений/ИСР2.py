# Дополнение программы задания тестами с использованием библиотеки doctest.

import json # импорт модуля json
from pprint import pprint #импорт функции pprint (для более красвного отображения)
 
with open('MOCK_DATA.json', 'r') as f: # открытие json файла для чтения. задаем псведоним f
    text = json.load(f) # загрузка содержимого

print("{0:}{1:^18}{2:^30}{3:^33}{4:^16}".format('ID', 'First name', 'E-mail', 'Gender', 'IP address')) # заголовок
for txt in text:
     print("{0:}{1:^18}{2:^30}{3:^33}{4:^16}".format(txt['id'], txt['first_name'], txt['email'], txt['gender'], txt['ip_address'])) #форматный вывод всех значений

try:
    import json
except ImportError:
    print("Ошибка при попытке импартировать модуль")

    try:
        for element in data:
            for item in element:
                try:
                    print(item,' : ',element.get(item))
                except KeyError:
                    print('Неверное взятие по ключу')
    except IndexError:
            print('Неверное итерирование по объекту')
try:
    with open("data.json", "r") as read_file:
        try:
            data = json.load(read_file)
        except json.JSONDecodeError:
            print("не json")

        dataPrint(data)

except FileNotFoundError:
    print("все норм")
except IOError:
    print("")
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()