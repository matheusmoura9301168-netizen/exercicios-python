# Menu de operações sobre um array NumPy.

import numpy as np

arr = np.array(["a", "b", "c", "d", "e", "f", "g"])

while True:
    print("\nMenu:")
    print("10 - Ver Array")
    print("1  - Adicionar item no fim do array")
    print("2  - Adicionar item em alguma posição do array")
    print("3  - Remover item do array")
    print("4  - Remove o último item do array e retorna-o")
    print("5  - Ordena o array por ordem crescente")
    print("6  - Inverte as posições dos itens")
    print("7  - Contar algum item")
    print("8  - Mostrar array sem elementos repetidos")
    print("9  - Remove todos os elementos do array")
    print("0  - Sair")

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            add_item = input("Insira o item: ")
            arr = np.append(arr, add_item)

        case "2":
            add_item = input("Insira o item: ")
            pos = int(input("Posição do item: "))
            arr = np.insert(arr, pos, add_item)

        case "3":
            print(arr)
            remove_item = input("Insira o item que quer remover: ")
            arr = arr[arr != remove_item]

        case "4":
            if arr.size > 0:
                print("Removido:", arr[-1])
                arr = arr[:-1]
            else:
                print("Array vazio!")

        case "5":
            arr = np.sort(arr)

        case "6":
            arr = arr[::-1]

        case "7":
            item = input("Insira o item que quer contar: ")
            n = np.count_nonzero(arr == item)
            print(f"O item '{item}' aparece {n} vezes no array")

        case "8":
            elementos_unicos = np.unique(arr)
            print("Array sem repetidos:", elementos_unicos)

        case "9":
            arr = np.array([])

        case "10":
            print("Array atual:", arr)

        case "0":
            break

        case _:
            print("Opção inválida, tente novamente.")
