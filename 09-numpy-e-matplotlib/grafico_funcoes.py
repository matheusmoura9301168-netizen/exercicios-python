# Funções linear, quadrática e cúbica no mesmo gráfico.

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2, 100) # intervalo em x de 0 a 2. O 100 significa que desenha 100 pontos e faz a união entre eles.

#plt.figure(figsize=(5, 2.7), layout='constrained’) #tamanho da figura - 5 por 2.7 e restringe o gráfico ao espaço
plt.plot(x, x, label='linear')#função linear y=x
plt.plot(x, x**2, label='quadrático')#função quadrática y=x**2
plt.plot(x, x**3, label='cúbico')#função cubica y=x**3
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Gráfico simples")
plt.legend()
plt.show ()
