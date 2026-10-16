# A mesma validação dentro de uma função.

import re
def valida(numero):
 if re.match(r"\((\d{3})\)\s*([1-9][0-9]{5})$|^(9\d{8})$", numero):
    return numero
 else:
    print("numero de telefone inválido")
 return None
while True:
 telefone = input("Numero de telefone: ")
 if valida(telefone):
    break
print(valida(telefone))
