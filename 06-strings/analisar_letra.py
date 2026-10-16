# Quantas vezes aparece a letra E e em que posições.

frase = input("Digite uma frase: ")

quantidade = frase.lower().count("e")
primeira_pos = frase.lower().find("e")
ultima_pos = frase.lower().rfind("e")

print(f"A letra 'E' aparece {quantidade} vezes.")
print(f"A primeira ocorrência de 'E' está na posição {primeira_pos}.")
print(f"A última ocorrência de 'E' está na posição {ultima_pos}.")
