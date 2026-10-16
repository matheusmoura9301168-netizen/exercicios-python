# Exercícios com uma agenda: inserir, consultar e filtrar.

import sqlite3

DB_NAME = "BDs/agenda.db"

def ex1():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agenda (
            nome TEXT,
            telefone TEXT
        )
    """)
    # Inserir um registo
    cursor.execute("INSERT INTO agenda (nome, telefone) VALUES (?, ?)", ("João Silva", "123456789"))
    conn.commit()
    conn.close()
    print("Exercício 1 concluído: tabela criada e registo inserido.")

def ex2():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agenda")
    registo = cursor.fetchone() # devolve apenas o próximo registo desse buffer, como uma tupla.
    print("Primeiro registo:", registo)
    conn.close()

def ex3():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    tupla = ("Maria Santos", "987654321")
    cursor.execute("INSERT INTO agenda (nome, telefone) VALUES (?, ?)", tupla)
    conn.commit()
    conn.close()
    print("Exercício 3 concluído: tupla inserida.")

def ex4():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agenda WHERE nome LIKE 'M%'")
    registo = cursor.fetchone()
    while registo:
        print(registo)
        registo = cursor.fetchone()
    conn.close()

def ex5():
    nome_pesquisa = input("Digite o nome a pesquisar: ")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agenda WHERE nome=?", (nome_pesquisa,))
    registo = cursor.fetchone()
    while registo:
        print(registo)
        registo = cursor.fetchone()
    conn.close()

def ex6():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agenda")
    for registo in cursor.fetchall():
        print(registo)
    conn.close()

def ex7():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE agenda SET telefone=? WHERE nome=?", ("111111111", "João Silva"))
    conn.commit()
    conn.close()
    print("Exercício 7 concluído: registo atualizado.")

def ex8():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE agenda SET telefone=? WHERE nome=?", ("222222222", "Maria Santos"))
        raise Exception("Erro simulado para rollback") #serve para forçar um erro artificialmente durante a execução.
        conn.commit()
    except:    # Se qualquer erro ocorrer dentro do bloco "try:" o programa entra aqui.
        conn.rollback()
        print("Rollback efetuado.")
    finally: # sempre é executado, independentemente de ter havido erro ou não.
        conn.close()

def ex9():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM agenda WHERE nome=?", ("Irene Pereira",))
    conn.commit()
    conn.close()
    print("Exercício 9 concluído: registo apagado.")

def menu():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("CREATE TABLE IF NOT EXISTS agenda (nome TEXT, telefone TEXT)")
    conn.close()
    while True:
        print("\n    MENU")
        print("1 - Exercício 1 (Criar BD e inserir registo)")
        print("2 - Exercício 2 (Mostrar primeiro registo)")
        print("3 - Exercício 3 (Inserir tupla)")
        print("4 - Exercício 4 (Listar com condição - While)")
        print("5 - Exercício 5 (Pesquisar registos - While)")
        print("6 - Exercício 6 (Listar todos - For)")
        print("7 - Exercício 7 (Update registo)")
        print("8 - Exercício 8 (Update com rollback)")
        print("9 - Exercício 9 (Delete registo Irene Pereira)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            ex1()
        elif opcao == "2":
            ex2()
        elif opcao == "3":
            ex3()
        elif opcao == "4":
            ex4()
        elif opcao == "5":
            ex5()
        elif opcao == "6":
            ex6()
        elif opcao == "7":
            ex7()
        elif opcao == "8":
            ex8()
        elif opcao == "9":
            ex9()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida.")

while True:
    menu()
