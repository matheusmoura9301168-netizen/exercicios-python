# Obriga a introduzir nome e apelido.

import re
while True:
 # Validação do Nome Completo
 nome = input("Digite o nome completo do aluno: ")
 if re.match(r"^[A-Za-zÀ-ÿ]+ [A-Za-zÀ-ÿ\s]+$"  r"$", nome):
    break
 else:
    print("Erro")
