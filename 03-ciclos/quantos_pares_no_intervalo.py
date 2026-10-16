# Conta os números pares de um intervalo.

inicio = int(input("Introduza o número inicial: "))
fim = int(input("Introduza o número final: "))

contador = 0
for i in range(inicio, fim + 1):
    if i % 2 == 0:
        contador += 1

print(f"Entre {inicio} e {fim} há {contador} números pares.")
