# Menu de operações sobre uma lista com contador de elementos.

lista = [50]
n = 1
while True:
    print("\nMenu:")
    print("10- Ver Lista")
    print("1 - Adicionar item no fim da lista")
    print("2 - Adicionar item em alguma posiçao da lista")
    print("3 - Remover item da lista")
    print("4 - Remove o último item da lista e retorna-o")
    print("5 - Ordena a lista por ordem crescente")
    print("6 - Inverte as posições dos itens")
    print("7 - Contar algum item")
    print("8 - mostrar lista sem elementos repetidos")
    print("9 - Remove todos os elementos da lista.")
    print("n - Sair")
    print(f"lista composta de {n} elementos na lista")
    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            add_item = input("Insira o item: ")
            lista.append(add_item)
            n=n+1
        case "2":
            add_item = input("Insira o item: ")
            po = int(input("Posição do item: "))
            lista.insert(po, add_item)
            n=n+1
        case "3":
            print(lista)
            remove_item = input("Insira o item que quer remover: ")
            if remove_item in lista:
                lista.remove(remove_item)
                n=n-1
            else:
                print("Esse item não está na lista.")
        case "4":
            if lista:
                print(lista.pop())
                n=n-1
            else:
                print("A lista está vazia.")
        case "5":
            lista.sort()
        case "6":
            lista.reverse()
        case "7":
            item = input("Insira o item que quer contar: ")
            m = lista.count(item)
            print(f"A string existe {m} vezes na lista")
        case "8":
            elementos_unicos = set(lista)
            print(elementos_unicos)
        case "9":
            lista.clear()
            n=0
        case "10":
            print(lista)
        case "n":
            break
