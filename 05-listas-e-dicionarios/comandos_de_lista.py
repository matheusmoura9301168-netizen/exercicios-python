# Menu com os principais métodos de listas.

lista = ["a", "b", "c", "d", "e", "f", "g"]
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
    print("0 - Sair")
    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            add_item = input("Insira o item: ")
            lista.append(add_item)
        case "2":
            add_item = input("Insira o item: ")
            po = int(input("Posição do item: "))
            lista.insert(po, add_item)
        case "3":
            print(lista)
            remove_item = input("Insira o item que quer remover: ")
            if remove_item in lista:
                lista.remove(remove_item)
            else:
                print("Esse item não está na lista.")
        case "4":
            if lista:
                print(lista.pop())
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
        case "10":
            print(lista)
        case "0":
            break
