# O mesmo exercício usando funções.

soma = 0
media = 0
num = 0
def soma1():
    global soma, num
    soma+=num

def media1():
    global soma, n, media
    media = soma/n

n = int(input( "Digite quantos numero inteiro quer digitar: " ))
for i in range(n):
    num = float(input("Indique um valor numerico (inteiro/real): "))
    soma1()
media1()
print(f"Forma digitados {n} numeros e a sua soma é = {soma}")
print(f"A maedia dos valores indicados é: {media}")
