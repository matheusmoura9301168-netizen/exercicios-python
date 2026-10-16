# Raízes de uma equação do 2.º grau.

import math

def calcular():
    print("Equação do tipo ax^2 + bx + c = 0")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    if a == 0:
        print("Não é uma equação de segundo grau (a deve ser diferente de 0).")
        return

    delta = b**2 - 4*a*c

    if delta < 0:
        print("esta equação não possui raízes reais")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"a raiz dupla desta equação é {raiz}")
    else:
        raiz1 = (-b - math.sqrt(delta)) / (2*a)
        raiz2 = (-b + math.sqrt(delta)) / (2*a)

        x, y = sorted([raiz1, raiz2])
        print(f"as raízes da equação são {x} e {y}")

calcular()
