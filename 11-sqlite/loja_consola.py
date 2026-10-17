# Loja na consola com clientes, fornecedores, produtos e pedidos.

import sqlite3   # Biblioteca para trabalhar com SQLite
import sys       # Usada para encerrar o programa
import time      # Usada para simular pausas (como Sleep no C)
from pathlib import Path  # Usada para garantir que o diretório do banco exista

# Caminho do banco de dados
DB_PATH = "BDs/Loja.db"

# Criar diretório automaticamente se não existir
Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)

# Conectar ao banco de dados SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
# Ativar integridade referencial (chaves estrangeiras funcionarem corretamente)
cursor.execute("PRAGMA foreign_keys = ON;")

# Criação das tabelas

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Fornecedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    contato TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT NOT NULL,
    fornecedor_id INTEGER,
    FOREIGN KEY (fornecedor_id) REFERENCES Fornecedores(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    data TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id) ON DELETE CASCADE,
    FOREIGN KEY (produto_id) REFERENCES Produtos(id) ON DELETE CASCADE
);
""")

conn.commit()

# Funções auxiliares
def cadastrar_cliente(nome, senha):
    #Insere um novo cliente na tabela Clientes
    try:
        cursor.execute("INSERT INTO Clientes (nome, senha) VALUES (?, ?)", (nome.strip(), senha.strip()))
        conn.commit()
        print("Cliente cadastrado com sucesso.")
        time.sleep(2)
    except sqlite3.IntegrityError:
        print("⚠️ Esse nome já existe, faça login ou escolha outro.")
        time.sleep(5)

def autenticar_cliente(nome, senha):
    #Verifica se nome e senha existem na tabela Clientes
    cursor.execute("SELECT id FROM Clientes WHERE nome=? AND senha=?", (nome.strip(), senha.strip()))
    row = cursor.fetchone()
    return row[0] if row else None

def cadastrar_fornecedor(nome, contato):
    #Insere um fornecedor na tabela Fornecedores
    cursor.execute("INSERT INTO Fornecedores (nome, contato) VALUES (?, ?)", (nome.strip(), contato.strip()))
    conn.commit()

def cadastrar_produto(nome, preco, categoria, fornecedor_id):
    #Insere um produto na tabela Produtos
    cursor.execute(
        "INSERT INTO Produtos (nome, preco, categoria, fornecedor_id) VALUES (?, ?, ?, ?)",
        (nome.strip(), float(preco), categoria.strip(), fornecedor_id)
    )
    conn.commit()

def listar_produtos(categoria=None):
    #Lista produtos por categoria ou todos
    if categoria:
        cursor.execute("SELECT id, nome, preco FROM Produtos WHERE categoria=? ORDER BY id", (categoria,))
    else:
        cursor.execute("SELECT id, nome, preco, categoria FROM Produtos ORDER BY categoria, id")
    return cursor.fetchall()

def fazer_pedido(cliente_id, produto_id, quantidade):
    #Insere um pedido na tabela Pedidos
    cursor.execute(
        "INSERT INTO Pedidos (cliente_id, produto_id, quantidade) VALUES (?, ?, ?)",
        (cliente_id, produto_id, quantidade)
    )
    conn.commit()

def listar_pedidos_cliente(cliente_id):
    #Lista todos os pedidos de um cliente específico
    cursor.execute("""
    SELECT Produtos.nome, Pedidos.quantidade, Produtos.preco,
           (Pedidos.quantidade * Produtos.preco) AS total
    FROM Pedidos
    JOIN Produtos ON Pedidos.produto_id = Produtos.id
    WHERE Pedidos.cliente_id=?
    ORDER BY Pedidos.id
    """, (cliente_id,))
    return cursor.fetchall()

def listar_todos_pedidos():
    #Relatório geral de todos os pedidos da loja
    cursor.execute("""
    SELECT Pedidos.id, Clientes.nome, Produtos.nome, Produtos.categoria,
           Pedidos.quantidade, Produtos.preco,
           (Pedidos.quantidade * Produtos.preco) AS total, Pedidos.data
    FROM Pedidos
    JOIN Clientes ON Pedidos.cliente_id = Clientes.id
    JOIN Produtos ON Pedidos.produto_id = Produtos.id
    ORDER BY Pedidos.data DESC, Clientes.nome
    """)
    return cursor.fetchall()

def aplicar_desconto(valor, percentual=10):
    #Aplica desconto percentual sobre o valor
    return round(valor * (1 - percentual/100), 2)

def total_cliente(cliente_id):
    #Calcula o total gasto por um cliente
    cursor.execute("""
    SELECT SUM(Pedidos.quantidade * Produtos.preco)
    FROM Pedidos
    JOIN Produtos ON Pedidos.produto_id = Produtos.id
    WHERE Pedidos.cliente_id=?
    """, (cliente_id,))
    val = cursor.fetchone()[0]
    return round(val or 0.0, 2)


# Menus
def menu_principal():
    print("\n    G.L.Y.M.E.R.S")
    print("1. Modo Cliente (comprar)")
    print("2. Modo Administrador (relatórios)")
    print("3. Sair")
    return input("Escolha uma opção: ").strip()

def menu_categorias():
    print("\nCategorias de itens:")
    print("T. Talheres")
    print("M. Mesa")
    print("G. Guardanapos")
    print("P. Pratos")
    print("C. Copos")
    print("F. Finalizar compra")
    return input("Escolha uma categoria: ").strip().upper()

def exibir_produtos_categoria(categoria_codigo):
    #Mostra produtos de uma categoria específica
    mapa = {
        'T': 'Talheres',
        'M': 'Mesa',
        'G': 'Guardanapos',
        'P': 'Pratos',
        'C': 'Copos'
    }
    categoria = mapa.get(categoria_codigo)
    if not categoria:
        print("Categoria inválida.")
        return []

    produtos = listar_produtos(categoria)
    print(f"\nProdutos em {categoria}:")
    for pid, nome, preco in produtos:
        print(f"({pid}) {nome} - {preco:.2f} euros")
    return produtos

# Fluxo Cliente
def fluxo_cliente():
    print("\nBem-vindo ao Modo Cliente.\n")
    time.sleep(1)
    nome = input("Coloque um nome para login: ").strip()
    senha = input(f"{nome}, escolha uma senha para seu perfil: ").strip()
    cadastrar_cliente(nome, senha)
    time.sleep(2)

    cliente_id = None
    while cliente_id is None:
        tentativa = input(f"{nome}, qual é a sua senha para login: ").strip()
        cliente_id = autenticar_cliente(nome, tentativa)
        if cliente_id:
            print("Senha correta...\n")
            time.sleep(3)
        else:
            print("Senha incorreta! Tente novamente.")
            time.sleep(2)

    # Seleção por categorias
    while True:
        cate = menu_categorias()
        if cate == 'F':
            break

        produtos = exibir_produtos_categoria(cate)
        if not produtos:
            continue

        escolha = input("Digite o ID do produto (ou Enter para voltar): ").strip()
        if not escolha:
            continue
        try:
            produto_id = int(escolha)
            qtd = int(input("Quantidade: ").strip())
            if qtd <= 0:
                print("Quantidade deve ser maior que zero.")
                continue
            fazer_pedido(cliente_id, produto_id, qtd)
            print("Item adicionado ao carrinho!")
            time.sleep(0.8)
        except ValueError:
            print("Entrada inválida.")
        except sqlite3.IntegrityError:
            print("Esse produto não existe.")

    # Resumo e pagamento
    pedidos = listar_pedidos_cliente(cliente_id)
    if not pedidos:
        print("\nNenhum item comprado.")
        return

    print("\nResumo da compra:")
    for nome_prod, qtd, preco, total in pedidos:
        print(f"Produto: {nome_prod} | Qtd: {qtd} | Preço: {preco:.2f} | Total: {total:.2f}")

    total = total_cliente(cliente_id)
    print(f"\nPreço Final: {total:.2f} euros")
    print("\nEscolha um modo de pagamento:\n(1) Crédito\n(2) Débito\n(3) Refeição (10% desconto)")
    try:
        opc = int(input("Opção: ").strip())
    except ValueError:
        opc = 1  # Se o usuário digitar algo inválido, assume crédito

    if opc == 3:
        total_desc = aplicar_desconto(total, 10)
        print(f"Preço Final com Desconto: {total_desc:.2f} euros")
    else:
        print(f"Preço Final: {total:.2f} euros")

    print("\nObrigado por comprar na G.L.Y.M.E.R.S. Volte sempre!\n")

    # Fluxo Administrador

def fluxo_admin():
    print("\nBem-vindo ao Modo Administrador.\n")
    while True:
        print("1. Relatório geral de pedidos")
        print("2. Listar produtos por categoria")
        print("3. Inserir novo fornecedor")
        print("4. Inserir novo produto")
        print("5. Listar clientes")
        print("6. Voltar ao menu principal")

        op = input("\nEscolha uma opção: ").strip()
        if op == '1':
            pedidos = listar_todos_pedidos()
            if not pedidos:
                print("Nenhum pedido registrado.")
                continue
            print("\nRelatório Geral de Pedidos:")
            for pid, cliente, produto, categoria, qtd, preco, total, data in pedidos:
                print(f"#{pid} | {data} | Cliente: {cliente} | Produto: {produto} ({categoria}) | "
                      f"Qtd: {qtd} | Preço: {preco:.2f} | Total: {total:.2f}")
            tot_loja = sum(p[6] for p in pedidos)
            print(f"\nTotal Geral da Loja: {tot_loja:.2f} euros")

        elif op == '2':
            cate = menu_categorias()
            if cate == 'F':
                continue
            exibir_produtos_categoria(cate)

        elif op == '3':
            nome = input("Nome do fornecedor: ").strip()
            contato = input("Contato (email/telefone): ").strip()
            cadastrar_fornecedor(nome, contato)
            print("Fornecedor cadastrado.")

        elif op == '4':
            nome = input("Nome do produto: ").strip()
            try:
                preco = float(input("Preço: ").strip().replace(",", "."))
                print("Categoria: Talheres / Mesa / Guardanapos / Pratos / Copos")
                categoria = input("Informe a categoria: ").strip().title()
                fornecedor_id = int(input("ID do fornecedor: ").strip())
            except ValueError:
                print("Valor inválido. O preço e o ID do fornecedor têm de ser números.")
                continue
            cadastrar_produto(nome, preco, categoria, fornecedor_id)
            print("Produto cadastrado.")

        elif op == '5':
            cursor.execute("SELECT id, nome FROM Clientes ORDER BY id")
            clients = cursor.fetchall()
            if not clients:
                print("Nenhum cliente cadastrado.")
            else:
                for cid, nome in clients:
                    print(f"({cid}) {nome}")

        elif op == '6':
            break
        else:
            print("Opção inválida.")

# Loop Principal
def main_loop():
    # Aqui você pode chamar seed_data() se quiser inserir os produtos iniciais automaticamente
    # seed_data()
    while True:
        escolha = menu_principal()
        if escolha == '1':
            fluxo_cliente()
        elif escolha == '2':
            fluxo_admin()
        elif escolha == '3':
            print("Saindo... Obrigado!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    try:
        main_loop()
    finally:
        cursor.close()
        conn.close()
