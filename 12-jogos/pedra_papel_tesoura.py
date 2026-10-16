# Pedra, papel ou tesoura contra o computador.

import random
# 'p' = pedra, 'a' = papel, 't' = tesoura
opcoes = ['p', 'a', 't']
u = input().strip()
if u not in opcoes:
    print("opção inválida")
else:
    c = random.choice(opcoes)
    wins = {('p','t'), ('t','a'), ('a','p')}
    if u == c:
        resultado = 'empate'
    elif (u, c) in wins:
        resultado = 'ganha'
    else:
        resultado = 'perde'
    print(c, resultado)
