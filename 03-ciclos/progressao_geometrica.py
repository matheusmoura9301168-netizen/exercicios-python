# Termos e soma de uma progressão geométrica.

primeiro = int(input("Introduza o primeiro termo da P.G: "))
razao = int(input("Introduza a razão da P.G: "))

termo = primeiro
contador = 1
total = 0
limit = 5

while limit != 0:
    total = total + limit
    while contador <= total:
        print(termo, end=" ")
        termo = termo * razao
        contador = contador + 1
    print()
    limit = int(input("Quantos termos quer mostrar a mais? (0 para terminar): "))

# com razão 1 todos os termos são iguais e a fórmula dividiria por zero
if razao == 1:
    soma = primeiro * total
else:
    soma = primeiro * (razao**total - 1) // (razao - 1)
print("A soma de todos os termos mostrados é", soma)
