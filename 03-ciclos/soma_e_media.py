# Soma e média de n valores.

n = int(input( "Digite quantos numero inteiro quer digitar: " ))
soma = 0
for i in range(n):
    num = float(input("Indique um valor numerico (inteiro/real): "))
    soma+=num
media = soma/n
print(f"Forma digitados {n} numeros e a sua soma é = {soma}")
print(f"A maedia dos valores indicados é: {media}")
