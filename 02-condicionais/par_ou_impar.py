# Par ou ímpar agrupando casos no match.

def verificar_numero():
    numero = int(input("Digite um número entre 1 e 20: "))

    match numero:
        # Agrupando pares
        case 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20:
            print(f"O número {numero} é PAR.")
        # Agrupando ímpares
        case 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19:
            print(f"O número {numero} é ÍMPAR.")
        case _:
            print("Número fora do intervalo permitido (1 a 20).")


verificar_numero()
