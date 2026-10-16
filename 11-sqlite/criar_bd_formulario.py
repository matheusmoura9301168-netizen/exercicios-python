# Cria a base de dados usada pelo formulário de clientes.

import sqlite3

# cria/conecta à base de dados
conn = sqlite3.connect("BDs/clientes1.db")
c = conn.cursor()

# cria tabela "clientes" (id, nome, email)
c.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

conn.commit()
conn.close()
print("Base de dados criada com sucesso!")
