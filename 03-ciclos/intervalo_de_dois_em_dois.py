# Percorre um intervalo de dois em dois.

inicio = int(input("Introduza o número inicial (menor): "))
fim = int(input("Introduza o número final (maior): "))

for i in range(inicio, fim + 1, 2):
    print(i)
