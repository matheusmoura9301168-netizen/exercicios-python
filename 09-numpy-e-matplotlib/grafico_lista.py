# Lê 8 números, mostra o máximo e o mínimo e desenha o gráfico.

import matplotlib.pyplot as plt
import numpy as np

lista = []


for i in range(1,9):
    item = int(input(f"Digite um numero inteiro de indice {i-1}: "))
    lista.append(item)

print(lista)
arra = np.array(lista)

print("Máximo:", np.max(arra))
print("Mínimo:", np.min(arra))


plt.plot(arra)
plt.ylabel('números da lista')
plt.show()
