# As operações aritméticas com dois inteiros.

# Solicita dois números inteiros
a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))

# Realiza as operações
print(f"Soma: {a + b}")
print(f"Subtração: {a - b}")
print(f"Multiplicação: {a * b}")
print(f"Divisão: {a / b if b != 0 else 'Divisão por zero não permitida'}")
print(f"Divisão inteira: {a // b if b != 0 else 'Divisão por zero não permitida'}")
print(f"Resto da divisão: {a % b if b != 0 else 'Divisão por zero não permitida'}")
