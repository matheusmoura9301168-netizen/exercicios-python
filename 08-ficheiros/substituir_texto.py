# Copia um ficheiro para outro substituindo um texto.

ficheiro_origem = input("Introduza o nome do primeiro ficheiro: ")
ficheiro_destino = input("Introduza o nome do segundo ficheiro: ")
string1 = input("Introduza a string1: ")
string2 = input("Introduza a string2: ")

origem = open(ficheiro_origem, "r")
conteudo = origem.read()
origem.close()

conteudo_modificado = conteudo.replace(string1, string2)

destino = open(ficheiro_destino, "w")
destino.write(conteudo_modificado)
destino.close()

print(f"Substituição concluída. Conteúdo gravado em '{ficheiro_destino}'.")
