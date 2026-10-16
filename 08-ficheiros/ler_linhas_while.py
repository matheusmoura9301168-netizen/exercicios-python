# Lê linha a linha com while.

fich = open("dados/teste.txt", "r")
linha = fich.readline()

while linha:
    print(linha, end = "")
    linha = fich.readline()
