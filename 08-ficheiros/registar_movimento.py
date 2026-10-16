# Acrescenta um movimento à lista de compras.

valor = input("Introduza o valor (ex: -53.5 ou +20): ")
descricao = input("Introduza a descrição (ex: fruta, vale): ")

fich = open("dados/compras_supermercado.txt", "a")
fich.write(f"{valor} {descricao}\n")

print("Linha adicionada com sucesso.")
