# Funções de leitura com validação dos números e da operação.

def Num01():
    while True:
        try:
            n1 = float(input("Primeiro número:"))
            break
        except ValueError as erro:
            print("Erro: Inseriu um caracter em vez de ser um numero")
        except Exception as erro:
            print(erro)
    return n1

def Num02():
    while True:
        try:
            n2 = float(input("Segundo número:"))
            break
        except ValueError as erro:
            print("Erro: Inseriu um caracter em vez de ser um numero")
        except Exception as erro:
            print(erro)
    return n2

def Operacao():
    while True:
        operacao = input("Digite a operação a realizar (+, -, * ou /):")
        if operacao in ("+", "-", "/", "*"):
            if operacao == "+":
                return '+'
            elif operacao == "-":
                return '-'
            elif operacao == "*":
                return '*'
            elif operacao == "/":
                return '/'
        else:
            print("Operação inválida!")
