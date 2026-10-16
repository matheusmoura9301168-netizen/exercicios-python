# Label com fonte, cor de fundo e largura.

from tkinter import *

# Inicializa a janela principal
menu_inicial = Tk()
menu_inicial.title("Titulo")               # Define o título da janela
menu_inicial.geometry("500x300")           # Define o tamanho da janela

# Cria o label com propriedades visuais
label_2 = Label(menu_inicial,
                text="Este é o label 2",
                font="Arial 40",
                bg="red",
                width=20)
label_2.pack()  # Adiciona o label à janela

# Inicia o loop principal da interface
menu_inicial.mainloop()
