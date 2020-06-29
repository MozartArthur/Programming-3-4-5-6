import pandas as pd
import numpy as nu

f = pd.read_csv('Значения.csv', sep=';', encoding='utf-8', index_col="id")

sz = nu.mean(f['data'])  
ds = nu.var(f['data'])  
so = nu.std(f['data'])   

print("Ср.знач = ", sz, "\n Дисперсия = ", ds, "\n Ст. отклонение = ", so)