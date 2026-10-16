# Botão que chama uma função com argumento (lambda).

from tkinter import *

# Inicializa a janela principal
menu_inicial = Tk()
menu_inicial.title("Titulo")               # Define o título da janela
menu_inicial.geometry("500x300")           # Define o tamanho da janela

# Função que recebe uma mensagem como argumento e imprime no console
def cmd_Click(mensagem):
    print(mensagem)

# Cria o botão e associa à função com argumento usando lambda
cmd = Button(menu_inicial, text="Executar", command=lambda: cmd_Click("Nova mensagem"))
cmd.pack()                                 # Adiciona o botão à janela

# Inicia o loop principal da interface
menu_inicial.mainloop()
