# Inverte os dígitos de um número.

def inver(numero):
    return int(str(numero)[::-1])


num = int(input("Digite um número inteiro: "))
print(f"O número invertido é {inver(num)}")
