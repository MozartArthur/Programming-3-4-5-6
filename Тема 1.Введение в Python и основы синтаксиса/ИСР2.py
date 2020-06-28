import math #подключение модуля match для вычисления корня

def Geron(a, b, c): # создание функции
    p=(a+b+c)/2 #полупириметр
    return math.sqrt(p*(p-a)*(p-b)*(p-c)) # возвращение значения площади

print(Geron(3, 4, 5)) # пример
 