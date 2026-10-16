# Mostra os números pares de um intervalo.

inicio = int(input("Introduza o número inicial: "))
fim = int(input("Introduza o número final: "))

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        print(i)
