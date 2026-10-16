# Ecrã de login centrado na janela.

from tkinter import *

# Inicializa a janela principal
root = Tk()
root.title("Login")

# Define tamanho da janela
largura_janela = 300
altura_janela = 150

# Calcula posição para centralizar
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

# Aplica geometria centralizada
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Layout com .grid()
Label(root, text="Usuário:").grid(row=0, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Senha:").grid(row=1, column=0, sticky=W, padx=10, pady=5)

text_usuario = Entry(root)
text_usuario.grid(row=0, column=1, padx=10, pady=5)

text_senha = Entry(root, show="*")
text_senha.grid(row=1, column=1, padx=10, pady=5)

cmd_login = Button(root, text="Login")
cmd_login.grid(row=2, column=1, sticky=E, padx=10, pady=10)

# Inicia o loop principal da interface
root.mainloop()
