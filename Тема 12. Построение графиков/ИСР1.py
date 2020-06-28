matplotlib inline
import numpy as np
import math
import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv('CENA.csv', header = None) #Загружаем данные из csv-файла в скрипт с помощью метода read_csv модуля pandas.
l, k = df[0], df[1]

plt.scatter(l, k, c ='black')

lis = list(l)
lis2 = list(k)