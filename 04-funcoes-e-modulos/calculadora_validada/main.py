# Programa principal que importa o módulo MD_CC.

import MD_CC

n1 = MD_CC.Num01()
n2 = MD_CC.Num02()
op = MD_CC.Operacao()
n = 1

while n:
    n = 1
    if op == "+":
        resultado = n1 + n2
        break
    elif op == "-":
        resultado = n1 - n2
        break
    elif op == "*":
        resultado = n1 * n2
        break
    elif op == "/":
        while True:
            try:
                resultado = n1 / n2
                n = 0
                break
            except ZeroDivisionError as erro:
                print("Não pode dividir por Zero(0)")
                n2 = MD_CC.Num02()
            except Exception as erro:
                print(erro)

print(f"{n1} {op} {n2} = {resultado:.2f}")
