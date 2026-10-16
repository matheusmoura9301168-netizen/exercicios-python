# Verifica se um texto representa um número inteiro ou decimal.

import re

def numero_valido(s):
    padrao = r'^[+-]?\d+(\.\d+)?$'
    return bool(re.match(padrao, s))

# Testes
testes = ["10", "+5", "-3", "-10.3", "0.80", "2.8033", "abc", "10.", ".5"]
for t in testes:
    print(f"{t}: {numero_valido(t)}")
