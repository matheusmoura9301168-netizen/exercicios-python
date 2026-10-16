# Posicionamento com grid.

from tkinter import *

# Inicializa a janela principal
root = Tk()
root.title("Título")

#Linha 0: duas labels lado a lado
Label(root, width=20, bg="red").grid(row=0, column=0)
Label(root, width=20, bg="green").grid(row=0, column=1)

# Linha 1: label azul que ocupa duas colunas e se estica horizontalmente
Label(root, width=40, bg="blue").grid(row=1, column=0, columnspan=2, sticky='we')

#Inicia o loop principal da interface
root.mainloop()
