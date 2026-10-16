# Avalia expressões escritas pelo utilizador até escrever 'sair'.

while True:
    e = input()
    if e == 'sair':
        break
    try:
        print(eval(e))
    except Exception as exc:
        print("erro:", exc)
