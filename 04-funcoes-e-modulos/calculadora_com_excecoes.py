# Calculadora com tratamento de exceções.

try:
    # Ler os números e converter para float
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
    operacao = input("Digite a operação a realizar (+, -, * ou /): ")
    match operacao:
        case "/":
            # Tratamento de divisão por zero
            try:
                resultado = a / b
            except ZeroDivisionError:
                print("⚠️ Erro: Divisão por zero não permitida!")
                resultado = None
        case "*":
            resultado = a * b
        case "+":
            resultado = a + b
        case "-":
            resultado = a - b
        case Exception as e:
            print(f"⚠️ Operação inválida!\nMotivo:({e})")
            resultado = None

    if resultado is not None:
        print("Resultado:", resultado)

# Captura de erros de conversão (quando o utilizador não insere números válidos)
except ValueError:
    print("⚠️ Erro: Deve introduzir números válidos!")

# Captura de qualquer outro erro inesperado
except Exception as e:
    print("⚠️ Erro inesperado:", e)
