# Primeiro e último nome, maiúsculas e minúsculas.

nome = input("Digite o seu nome completo: ").strip()

print("Nome em maiúsculas:", nome.upper())
print("Nome em minúsculas:", nome.lower())

partes = nome.split()
primeiro_nome = partes[0]
ultimo_nome = partes[-1]

print("Primeiro nome:", primeiro_nome)
print("Último nome:", ultimo_nome)
print("Quantidade de letras no primeiro nome:", len(primeiro_nome))
