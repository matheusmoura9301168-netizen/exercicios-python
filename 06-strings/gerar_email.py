# Gera um endereço de e-mail a partir do nome.

nome = input().strip().lower().replace(' ', '.')
dom = input().strip()
print(f"{nome}@{dom}")
