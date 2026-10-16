# A mesma calculadora organizada em funções.

def mostrar_menu():
    print("\n   CALCULADORA")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "5":
            print("Encerrando a calculadora...")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print(f"Resultado: {somar(num1, num2)}")
        elif opcao == "2":
            print(f"Resultado: {subtrair(num1, num2)}")
        elif opcao == "3":
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcao == "4":
            print(f"Resultado: {dividir(num1, num2)}")
        else:
            print("Opção inválida!")
main()
