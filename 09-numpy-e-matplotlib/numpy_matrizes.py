# Soma, produto e transposta de matrizes.

import numpy as np

mat1 = np.array([[1, 2],
                 [3, 4]])

mat2 = np.array([[5, 6],
                 [7, 8]])

print("Matriz 1:\n", mat1)
print("Matriz 2:\n", mat2)

# Operações
print("Soma das matrizes:\n", mat1 + mat2)
print("Multiplicação elemento a elemento:\n", mat1 * mat2)
print("Multiplicação matricial:\n", np.matmul(mat1, mat2))
print("Transposta da matriz 1:\n", mat1.T)
