# Fatorial com recursividade.

def f(n):
    return 1 if n <= 1 else n * f(n - 1)

n = int(input())
if n < 0:
    print("erro: n negativo")
else:
    print(f(n))
