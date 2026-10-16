# Potência calculada com um ciclo dentro de uma função.

def pot(base, expoente):

    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado


a = int(input("Digite a base (inteiro positivo): "))
b = int(input("Digite o expoente (inteiro positivo): "))
print(f"O resultado de {a}^{b} é {pot(a, b)}")
