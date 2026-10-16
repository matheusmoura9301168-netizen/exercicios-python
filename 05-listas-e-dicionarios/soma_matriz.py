# Soma de todos os elementos de uma matriz.

# lê 3 linhas com números separados por espaço (matriz 3xN ou 3x3, soma geral)
m = []
for _ in range(3):
    row = list(map(int, input().split()))
    m.append(row)
total = sum(sum(r) for r in m)
print(total)
