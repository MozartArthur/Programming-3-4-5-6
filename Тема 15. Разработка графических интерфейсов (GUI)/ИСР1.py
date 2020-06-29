import tkinter
from math import sqrt
from tkinter import *
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


x_list = []  #список с результатами полученных корней
values_list = []  #список вводимых значений

# определение корней
def solver(a,b,c):
    values_list.append(a)
    values_list.append(b)
    values_list.append(c)
        
    D = b**2 - 4*a*c     # дискриминант
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "Дискриминант равен: %s \n X1 = %s \n X2 = %s \n" % (D, x1, x2)
        x_list.append(x1)
        x_list.append(x2)
       
    else:
        text = "Дискриминант равен: %s \n Нет корней у данного уравнения" % D 
    return text


# отчистка поля ввода 
def inserter(value):
    output.delete("0.0","end")
    output.insert("0.0",value)

# проверка правильного ввода данных
def handler():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Введите 3 значения")

# отчистка поля ввода
def clear(event):
    caller = event.widget
    caller.delete("0", "end")


    
    
root = Tk() 
root.title("Квадратное уравнение")
root.minsize(425,330)
root.resizable(width=False, height=False)

frame = Frame(root) 
frame.grid()
 
a = Entry(frame, width=3)   
a.bind("<FocusIn>", clear)
a.grid(row=1, column=1,padx=(10,0)) 
 
a_lab = Label(frame, text="x**2+").grid(row=1,column=2)   
 

b = Entry(frame, width=3)   
b.bind("<FocusIn>", clear)
b.grid(row=1,column=3)

b_lab = Label(frame, text="x+").grid(row=1, column=4)  
 

c = Entry(frame, width=3)  
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)

c_lab = Label(frame, text="= 0").grid(row=1, column=6)  

but = Button(frame, text="Решить", command=handler).grid(row=1, column=7, padx=(10,0))

output = Text(frame, bg="#90DAB9", font="Arial 12", width=50, height=18)  

output.grid(row=2, columnspan=10)

root.mainloop()  

def roots(a,b,c):
    D = b ** 2 - 4 * a * c
    d = D ** 0.5
    x1 = (-b+d)/(2*a)
    x2 = (-b-d)/(2*a)
    if D > 0:
        return x1, x2
    elif x1 == x2:
        return x1
    else:
        exit('Сложные корни')
 
 