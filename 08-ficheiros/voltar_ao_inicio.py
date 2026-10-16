# Volta ao início do ficheiro com seek(0).

fich = open("dados/teste.txt", "r")

linha = fich.readline() # Lê uma linha (neste caso a 1ª)
print(linha, end = "")

fich.seek(0) # Voltando para o início do arquivo
linha = fich.readline() # Lê uma linha (neste caso a 1ª)
print(linha, end = "")

linha = fich.readline() # Lê uma linha (neste caso a 2ª)
print(linha, end = "")
