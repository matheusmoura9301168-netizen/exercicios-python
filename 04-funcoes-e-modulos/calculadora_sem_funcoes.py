# Calculadora com menu, sem funções.

print("    CALCULADORA")
print("1. Adição (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")
print("5. Sair")

while True:
    opcao = input("\nEscolha uma opção (1-5): ")

    if opcao == "5":
        print("Encerrando a calculadora...")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        print(f"Resultado: {num1 + num2}")
    elif opcao == "2":
        print(f"Resultado: {num1 - num2}")
    elif opcao == "3":
        print(f"Resultado: {num1 * num2}")
    elif opcao == "4":
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Erro: divisão por zero!")
    else:
        print("Opção inválida!")
