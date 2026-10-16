# Formulário de nome e morada dividido em frames.

from tkinter import *

# Inicializa a janela principal
root = Tk()
root.title("App")

# Criação das frames
frame_nome = Frame(root)
frame_morada = Frame(root)

# Widgets da frame_nome
label_nome = Label(frame_nome, text="Nome:")
label_apelido = Label(frame_nome, text="Apelido:")
text_nome = Entry(frame_nome)
text_apelido = Entry(frame_nome)

# Widgets da frame_morada
label_rua = Label(frame_morada, text="Rua:")
label_cidade = Label(frame_morada, text="Cidade:")
text_rua = Entry(frame_morada)
text_cidade = Entry(frame_morada)

# Botão de salvar
cmd_salvar = Button(root, text="Salvar")

# Layout horizontal dentro de cada frame
label_nome.grid(row=0, column=0, padx=5, pady=5)
text_nome.grid(row=0, column=1, padx=5, pady=5)
label_apelido.grid(row=0, column=2, padx=5, pady=5)
text_apelido.grid(row=0, column=3, padx=5, pady=5)

label_rua.grid(row=0, column=0, padx=5, pady=5)
text_rua.grid(row=0, column=1, padx=5, pady=5)
label_cidade.grid(row=0, column=2, padx=5, pady=5)
text_cidade.grid(row=0, column=3, padx=5, pady=5)

# Posicionamento das frames e botão na janela principal
frame_nome.grid(row=0, column=0, padx=10, pady=10)
frame_morada.grid(row=1, column=0, padx=10, pady=10)
cmd_salvar.grid(row=2, column=0, pady=10)

# Inicia o loop principal da interface
root.mainloop()
