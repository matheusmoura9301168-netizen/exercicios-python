# Controlo de stock de uma mercearia com dicionário.

stock = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]
}

while True:
    produto = input("Digite o produto vendido (ou 'fim' para terminar): ").lower()
    if produto == "fim":
        break
    if produto in stock:
        quantidade = int(input(f"Quantidade de {produto} vendida: "))
        if quantidade <= stock[produto][0]:
            stock[produto][0] -= quantidade
            print(f"{quantidade} unidades de {produto} vendidas.")
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print("Produto não encontrado.")

print("\nEstoque atualizado:")
for item, dados in stock.items():
    print(f"{item}: {dados[0]} unidades restantes, preço unitário €{dados[1]:.2f}")
