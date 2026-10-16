# Média, mediana e desvio padrão de uma matriz aleatória.

import numpy as np

#  3x3 com valores aleatórios entre 1 e 10
arr6 = np.random.randint(1, 11, size=(3, 3))

print("Array gerado:\n", arr6)

# Estatísticas
print("Média dos elementos:", np.mean(arr6))
print("Mediana dos elementos:", np.median(arr6))
print("Desvio padrão:", np.std(arr6))
print("Máximo:", np.max(arr6))
print("Mínimo:", np.min(arr6))

# Estatísticas por linha
print("Média por linha:", np.mean(arr6, axis=1))
print("Média por coluna:", np.mean(arr6, axis=0))
