# Registo, listagem e pesquisa de utilizadores.

def mostrar_menu():
    print("\n       MENU")
    print("1. Cadastrar novo usuário")
    print("2. Listar usuários")
    print("3. Buscar usuário por nome")
    print("4. Sair")


def cadastrar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    usuarios.append(nome)
    print(f"Usuário '{nome}' cadastrado com sucesso!")


def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for i, nome in enumerate(usuarios, start=1):
            print(f"{i}. {nome}")


def buscar_usuario(usuarios):
    busca = input("Digite o nome para buscar: ")
    encontrados = [u for u in usuarios if busca.lower() in u.lower()]
    if encontrados:
        print("Usuários encontrados:")
        for nome in encontrados:
            print(f"- {nome}")
    else:
        print("Nenhum usuário encontrado.")


def main():
    usuarios = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            listar_usuarios(usuarios)
        elif opcao == "3":
            buscar_usuario(usuarios)
        elif opcao == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
