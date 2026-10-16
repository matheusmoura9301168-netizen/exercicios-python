# Verifica se o nome contém o apelido Pereira.

nome = input("Digite o nome completo da pessoa: ").strip()

if "pereira" in nome.lower():
    print("O nome contém 'Pereira'.")
else:
    print("O nome NÃO contém 'Pereira'.")
