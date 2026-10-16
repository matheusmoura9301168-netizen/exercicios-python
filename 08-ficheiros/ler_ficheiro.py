# Lê um ficheiro inteiro.

fich = open("dados/teste.txt", "r")
texto = fich.read()
print(texto, end = "")
