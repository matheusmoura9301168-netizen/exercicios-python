# Operações entre dois arrays e produto escalar.

import numpy as np

arr4a = np.array([1, 2, 3])
arr4b = np.array([4, 5, 6])

print("Array A:", arr4a)
print("Array B:", arr4b)

print("Soma:", arr4a + arr4b)
print("Subtração:", arr4a - arr4b)
print("Multiplicação:", arr4a * arr4b)
print("Produto escalar:", np.dot(arr4a, arr4b))
