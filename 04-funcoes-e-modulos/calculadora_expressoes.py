# Avalia expressões escritas pelo utilizador até escrever 'sair'.

import re

print("Escreva uma conta (ex: 2*(3+4)) ou 'sair' para terminar.")
while True:
    e = input()
    if e == 'sair':
        break
    # só deixa passar números e operadores, para o eval não executar outro código
    if not re.fullmatch(r"[0-9+\-*/%.() ]+", e):
        print("erro: use apenas números e os operadores + - * / % ( )")
        continue
    try:
        print(eval(e))
    except Exception as exc:
        print("erro:", exc)
