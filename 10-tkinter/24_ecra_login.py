# Ecrã de login simples.

from tkinter import *

# Inicializa a janela principal
root = Tk()
root.title("Login")

# Labels
Label(root, text="Usuário:").grid(row=0, column=0, sticky=W)
Label(root, text="Senha:").grid(row=1, column=0, sticky=W)

# Entradas (mantidas em variáveis para uso posterior)
text_usuario = Entry(root)
text_usuario.grid(row=0, column=1)

text_senha = Entry(root, show="*")  # Adicionado show="*" para ocultar senha
text_senha.grid(row=1, column=1)

# Botão de login
cmd_login = Button(root, text="Login")
cmd_login.grid(row=2, column=1, sticky=E)

# Inicia o loop principal da interface
root.mainloop()
