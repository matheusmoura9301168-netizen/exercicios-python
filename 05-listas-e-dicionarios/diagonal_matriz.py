# Diagonal principal de uma matriz 3x3.

# lê 3x3 e imprime diagonal principal
m = [[int(x) for x in input().split()] for _ in range(3)]
print([m[i][i] for i in range(3)])
