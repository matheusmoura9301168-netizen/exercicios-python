# Mostra termos de uma PA enquanto o utilizador pedir mais.

primeiro = int(input("Introduza o primeiro termo da PA: "))
razao = int(input("Introduza a razão da PA: "))


termos_mostrados = 0
total_termos = 0
soma_termos = 0


limit = 10

while limit != 0:
    for i in range(termos_mostrados, termos_mostrados + limit):
        termo = primeiro + i * razao
        print(termo)
        soma_termos += termo
        total_termos += 1

    termos_mostrados += limit
    limit = int(input("Quantos termos adicionais deseja mostrar? (0 para terminar): "))


media = soma_termos / total_termos
print(f"\nForam mostrados {total_termos} termos.")
print(f"A média dos termos é {media:.2f}")
