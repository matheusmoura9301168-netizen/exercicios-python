# Percorre um intervalo com passo e conta os pares.

par = -2
def par1():
    global par
    if x % 2 == 0:
        par = par + 1
    else:
        return par


primeiro = int(input("Introduza o Limite Inferior: "))
razao = int(input("Introduza o numero para o passo (>0 Incremento): "))
n = int(input("Introduza o Limite superior: "))
x = 0
contador = 1
print(primeiro)
while x < n:
    par1()
    x = primeiro + (contador * razao)
    if  x <= n:
        print(x)
    else:
        print(f"No intervalo foram encotrado {par} numeros pares")
    contador = contador + 1
