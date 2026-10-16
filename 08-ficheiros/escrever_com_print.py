# Escreve num ficheiro usando print(file=...).

fich = open("teste3.txt", "w")
print("Utilizando a função print", file = fich)
fich.close()

fich = open("teste3.txt", "r")
texto = fich.read()
fich.close()

print(texto)
