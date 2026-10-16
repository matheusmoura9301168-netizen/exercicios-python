# Ordena uma lista e extrai os números pares.

lista = []
n = 0
lista1 = []
def m20():
    global lista1, add_item
    if add_item % 2 == 0:
        lista1.append(add_item)

while n < 10:
    add_item = int(input("Insira o item: "))
    lista.append(add_item)
    m20()
    print(lista)
    n += 1

print(f"Foram indicados os seguintes valores: {lista}")
lista.sort()
print(f"Lista ordenada: {lista}")
print(f"Lista de numeros pares: {lista1}")
