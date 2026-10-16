# Converte um número de 1 a 7 no dia da semana.

dia = int(input("Insira um número inteiro de (1 a 7): "))

match dia:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5:
        print("Sexta-feira")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número inválido. Por favor, insira um valor entre 1 e 7.")
