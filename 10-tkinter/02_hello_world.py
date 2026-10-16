# Janela com uma mensagem.

from tkinter import *

# Inicializa a janela principal
menu_inicial = Tk()
menu_inicial.title("Titulo")               # Define o título da janela
menu_inicial.geometry("500x300")           # Define o tamanho da janela

# Função que será chamada ao clicar no botão
def cmd_Click():
    print('Olá Mundo!')

# Cria o botão e associa à função cmd_Click
cmd = Button(menu_inicial, text="Executar", command=cmd_Click)
cmd.pack()                                 # Adiciona o botão à janela

# Inicia o loop principal da interface
menu_inicial.mainloop()
