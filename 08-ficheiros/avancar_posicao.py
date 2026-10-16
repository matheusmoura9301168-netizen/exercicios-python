# Avança a posição de leitura com seek e tell.

fich = open("dados/teste.txt", "r")

linha = fich.readline()
print(linha, end = "")

print("Posição =", fich.tell())  # Posição = 7

fich.seek(fich.tell() +3)  # avança 3 caracteres

linha = fich.readline()  # imprime a partir da posição 3
print(linha, end = "")

print("\nPosição =", fich.tell())  # Posição = 31
