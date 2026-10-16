# Conta pares e ímpares até ser introduzido 0.

pares = 0
impares = 0

num = int(input("Introduza um número inteiro (0 para terminar): "))

while num != 0:
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    num = int(input("Introduza um número inteiro (0 para terminar): "))

print("Foram introduzidos", pares, "números pares e", impares, "números ímpares.")
