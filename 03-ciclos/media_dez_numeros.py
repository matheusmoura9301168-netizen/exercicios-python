# Média de 10 números.

soma = 0
for i in range(10):
    num = int(input("Introduza o número : "))
    soma = soma + num

media = soma / 10
print(f"A média dos números inseridos é {media}")
