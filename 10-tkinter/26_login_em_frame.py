# Login organizado dentro de um Frame.

from tkinter import *

# Inicializa a janela principal
root = Tk()
root.title("App")

# 🔹 Cria a frame para o login
frame_login = Frame(root)
frame_login.grid(padx=20, pady=20)  # Adiciona espaçamento externo

# 🔹 Widgets dentro da frame
label_usuario = Label(frame_login, text="Usuário:")
label_password = Label(frame_login, text="Password:")
text_usuario = Entry(frame_login)
text_password = Entry(frame_login, show="*")  # 🔸 Adicionado: oculta senha
cmd_entrar = Button(frame_login, text="Entrar")

# 🔹 Layout com .grid() dentro da frame
label_usuario.grid(row=0, column=0, sticky=W, padx=5, pady=5)
text_usuario.grid(row=0, column=1, padx=5, pady=5)

label_password.grid(row=1, column=0, sticky=W, padx=5, pady=5)
text_password.grid(row=1, column=1, padx=5, pady=5)

cmd_entrar.grid(row=2, column=1, sticky=E, padx=5, pady=10)

# Inicia o loop principal da interface
root.mainloop()
