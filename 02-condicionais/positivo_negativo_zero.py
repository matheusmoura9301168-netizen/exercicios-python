# Indica se um número é positivo, negativo ou zero.

num = int(input("Digite um número: "))

match num:
    case num if num > 0:
        print("Positivo")
    case num if num < 0:
        print("Negativo")
    case _:
        print("Zero")
