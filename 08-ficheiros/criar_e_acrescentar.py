# Cria um ficheiro, acrescenta linhas e lê o conteúdo.

arq = open("teste2.txt", "a")
arq.write("Curso de Informática\n")
arq.write("Leiria\n")
arq.close()

arq = open("teste2.txt", "r")
texto = arq.read()
arq.close()

print(texto, end = "")
