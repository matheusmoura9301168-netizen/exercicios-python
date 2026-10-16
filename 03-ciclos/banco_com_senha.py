# Conta bancária simples protegida por senha.

s = 0.0
p = '1234'
if input() == p:
    while True:
        op = input()  # 'd' depositar, 'r' levantar, 's' saldo e sair
        if op == 'd':
            s += float(input())
        elif op == 'r':
            s -= float(input())
        elif op == 's':
            print(s)
            break
        else:
            print("opção inválida")
else:
    print("senha incorreta")
