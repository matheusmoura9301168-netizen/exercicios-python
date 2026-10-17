# Menu que usa o módulo calculadora.

import calculadora
while True:
 print("1. Soma")
 print("2. Subtração")
 print("3. Multiplicação")
 print("4. Divisão")
 print("0. Sair")
 op=int(input("Que operação deseja realizar: "))
 if op==0:
    break
 x=float(input("Primeiro numero: "))
 y=float(input("Segundo numero: "))
 if op==1:
    print("Soma:", calculadora.soma(x,y))
 elif op==2:
    print("Subtração:", calculadora.subtracao(x,y))
 elif op==3:
    print("Multiplicação:", calculadora.multiplicacao(x,y))
 elif op==4:
    print("Divisão:", calculadora.divisao(x,y))
 else:
    print("Opção inválida,tente novamente")
