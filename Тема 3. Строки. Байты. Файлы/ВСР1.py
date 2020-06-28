# Реализовать программу-игру «Угадай число», в которой для вывода на экран информации использовать метод format.
minX = 1 
maxX = 100 
while True:
    X = (minX+maxX)//2 
    number = input('Это {}?(да, больше, меньше)'.format(X))
    if number.lower() == 'да':
        print('Число {} угадано!'.format(X))
        break
    elif number=='больше':
        minX = X + 1
    else:
        maxX = X - 1