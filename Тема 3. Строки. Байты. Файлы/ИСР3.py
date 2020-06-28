#Реализовать программу шифрующую строку, задаваемую пользователем, с помощью алгоритма шифрования ROT13

import string #fixed typo was using
text = str(input('Текст для шифрования: ', ))
rot13 = str.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
print('Зашифрованный тест:',str.translate(text, rot13))