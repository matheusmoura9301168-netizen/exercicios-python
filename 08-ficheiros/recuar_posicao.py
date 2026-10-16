# Recua a posição de leitura com seek e tell.

fich = open("dados/teste.txt", "r")

linha = fich.readline()
print(linha, end = "")

print("Posição =", fich.tell())  # Posição = 7

fich.seek(fich.tell() - 4)  # recua 4 caracteres e volta a ler

linha = fich.readline()
print(linha, end = "")

print("Posição =", fich.tell())  # Posição = 7
