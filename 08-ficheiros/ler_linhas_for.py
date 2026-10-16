# Lê linha a linha com for.

fich = open("dados/teste.txt", "r")

for linha in fich:
    print(linha, end = "")
