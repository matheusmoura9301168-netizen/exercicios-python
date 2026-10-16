# Valida um número de telefone com regex.

import re
while True:
    telefone = input("Numero de telefone: ").strip()
    if re.match(r"\((2\d{2})\)\s*([1-9]{1}[0-9]{5})$|^(9\d{8})$", telefone):
        print("Nº válido")
        break
    else:
        print("numero de telefone inválido")
