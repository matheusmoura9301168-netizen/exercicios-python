# Lê apenas os três primeiros caracteres.

fich = open("dados/teste.txt", "r")
texto = fich.read(3)
print(texto)
