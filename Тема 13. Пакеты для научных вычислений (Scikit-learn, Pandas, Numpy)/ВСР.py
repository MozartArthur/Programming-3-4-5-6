import threading
import numpy as np

def multi(matrix1, matrix2, n):
  matrix3 = np.zeros((n,n)) 
  lst = []
  for i in range(n):
    for j in range(n):
      row = matrix1[i] 
      col = matrix2[j] 
      elem = sum([a*b for a,b in zip(row,col)])
      matrix3[i][j]=elem 
  return matrix3

if __name__ == "__main__":
  X = int(input("Введите размерность: "))
  A = np.random.randint(10, size=(X,X))
  print(A, "\n")
  B = np.random.randint(10, size=(X,X))
  print(B, "\n")

  threading.Thread(target=lambda a, b, n:print(multi(a,b,n)),args=(A, B, X)).start() 