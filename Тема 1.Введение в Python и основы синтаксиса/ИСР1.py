# Разработка скрипта, вычисляющего сумму первых n-членов арифметической прогрессии (использование функций, условных операторов)

def Progress(a, h, n): #n - кол-во членов, h - шаг, a - первый член
    if h == 1:
        return a
    else:
        return a+(n-1)+h+Progress(a, h, n-1) 
 
print (Progress(1, 2, 6)) # Первый член = 1, шаг = 2, кол-во членов - 6