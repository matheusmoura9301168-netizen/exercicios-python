# Valores abaixo da média.

valores = []
for i in range(6):
    numero = float(input(f"Digite o {i+1}º número real: "))
    valores.append(numero)

media = sum(valores) / len(valores)


print(f"\nMédia aritmética: {media:.2f}")
print("Valores menores que a média:")

for v in valores:
    if v < media:
        print(v)
