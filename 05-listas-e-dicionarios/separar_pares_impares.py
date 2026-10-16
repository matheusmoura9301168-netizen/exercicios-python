# Separa números pares e ímpares em listas diferentes.

valores = []
pares = []
impares = []


for i in range(12):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    valores.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)


print("\nVetor completo:", valores)
print("Vetor PAR:", pares)
print("Vetor ÍMPAR:", impares)
