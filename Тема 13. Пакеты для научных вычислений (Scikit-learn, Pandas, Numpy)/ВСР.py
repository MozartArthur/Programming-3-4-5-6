import cython
def cy_dot_product(X, Y):
   xrows, xcols = X.shape
   yrows, ycols = Y.shape
   Z = Matrix.zeros((xrows, ycols))
   Yt = Y.transpose()
   for i, (Xi, Zi) in enumerate(zip(X, Z)):
      for k, Ytk in enumerate(Yt):
            Zi[k] = sum(Xi[j] * Ytk[j]
                        for j in range(xcols))

   return Z
