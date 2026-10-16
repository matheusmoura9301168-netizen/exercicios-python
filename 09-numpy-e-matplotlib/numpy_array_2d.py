# Array bidimensional: dimensões e formato.

import numpy as np

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("Array bidimensional:\n", arr2)
print("Dimensões:", arr2.ndim)
print("Formato:", arr2.shape)
print("Elemento [1,2]:", arr2[1, 2])  # linha 1, coluna 2
