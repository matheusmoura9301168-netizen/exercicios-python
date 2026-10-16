# Adicionar, listar, procurar e remover clientes.

import sqlite3
import time
import sys

DB = "BDs/clientes.db"

with sqlite3.connect(DB) as _conn:
    _conn.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, email TEXT NOT NULL)")

def proximo_id_livre():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id FROM clientes ORDER BY id")
    ids = [row[0] for row in c.fetchall()]
    conn.close()
    id = 1
    while id in ids:
        id += 1
    return id

def adicionar_cliente(nome, email):
    novo_id = proximo_id_livre()
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)", (novo_id, nome, email))
    conn.commit()
    conn.close()
    print(f"Cliente adicionado com ID {novo_id}.")
    time.sleep(2)

def listar_clientes():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, nome, email FROM clientes")
    clientes = c.fetchall()
    conn.close()
    print("Lista de clientes:")
    for id_, nome, email in clientes:
        print(f"{id_}: {nome} - {email}")
    time.sleep(2)

def procurar_cliente(nome):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, nome, email FROM clientes WHERE nome LIKE ?", (f"%{nome}%",))
    clientes = c.fetchall()
    conn.close()
    if clientes:
        print("Resultados encontrados:")
        for id_, n, email in clientes:
            print(f"{id_}: {n} - {email}")
    else:
        print("Nenhum cliente encontrado.")
    time.sleep(2)

def remover_cliente(id_):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM clientes WHERE id = ?", (id_,))
    conn.commit()
    conn.close()
    print(f"Cliente com ID {id_} removido.")
    time.sleep(2)

def menu():
    print("\nMenu:")
    print("1 - Adicionar cliente")
    print("2 - Listar clientes")
    print("3 - Procurar cliente")
    print("4 - Remover cliente")
    print("0 - Sair")
    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            nome = input("Nome: ")
            email = input("Email: ")
            adicionar_cliente(nome, email)
        case "2":
            listar_clientes()
        case "3":
            nome = input("Nome a procurar: ")
            procurar_cliente(nome)
        case "4":
            id_ = input("ID do cliente a remover: ")
            remover_cliente(id_)
        case "0":
            print("Saindo...")
            time.sleep(2)
            sys.exit()
        case _:
            print("Opção inválida.")

while True:
    menu()
