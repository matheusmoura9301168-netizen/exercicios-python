# Adivinhar um número até 1000 com pontuação.

import random
n = random.randint(1, 1000)
t = 100
print("começe com um numero de 0 a 1000: ")

while t > 0:
    try:
        x = int(input())
    except:
        print("entrada inválida")
        continue
    if x == n:
        print('Acertou')
        print('Pontuação:', t)
        break
    elif x < n:
        print('Maior')
    else:
        print('Menor')
    t -= 1
else:
    print('Fim das tentativas. Número:', n)
