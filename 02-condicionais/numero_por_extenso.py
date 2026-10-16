# Mostra por extenso números de 1 a 6, agrupados aos pares.

num = int(input("Digite um número entre 1 e 6: "))

match num:
    case 1 | 2:
        print("Um ou Dois")
    case 3 | 4:
        print("Três ou Quatro")
    case 5 | 6:
        print("Cinco ou Seis")
    case _:
        print("Número fora do intervalo permitido")
