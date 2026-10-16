# Calculadora com match-case.

def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    match operacao:
        case "+":
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        case "-":
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        case "*":
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        case "/":
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
            else:
                print("Erro: divisão por zero não é permitida.")
        case _:
            print("Operação inválida. Use apenas +, -, *, /.")

calculadora()
