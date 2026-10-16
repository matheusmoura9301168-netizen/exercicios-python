# Mostra uma imagem dentro de um Label (precisa de img/nome.png).

from tkinter import *

# Inicializa a janela principal
root = Tk()
root.title("Imagem na Label")

#Carrega a imagem (certifique-se de que o caminho está correto)
img = PhotoImage(file="img/nome.png")

#  Cria a label com a imagem
label_imagem = Label(root, image=img)
label_imagem.pack()

#Importante: manter referência à imagem
label_imagem.image = img

# Inicia o loop principal da interface
root.mainloop()
