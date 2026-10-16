# Calcula o saldo final a partir dos movimentos do ficheiro.

saldo = 0
descri = ""
fich = open("dados/compras_supermercado.txt", "r")
for linha in fich:
    valor, descri = linha.strip().split(" ", 1)
    saldo += float(valor)

print(f"O saldo após as compras no supermercado é de {saldo} euros")
