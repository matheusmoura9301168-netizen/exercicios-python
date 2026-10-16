# Área e perímetro de um círculo.

import math
# Solicita o raio ao utilizador
raio = float(input("Digite o raio do círculo: "))

# Calcula área e perímetro
area = math.pi * raio ** 2
perimetro = 2 * math.pi * raio

# Exibe os resultados
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")
