# Lista as propriedades disponíveis de um Label.

from tkinter import *

# Inicializa a janela principal
menu_inicial = Tk()
menu_inicial.title("Label como dicionário")

# Cria uma label simples
label1 = Label(menu_inicial, text="Menu Principal")
label1.pack()

# Imprime no terminal todas as chaves disponíveis para o widget Label
print(label1.keys())

# Inicia o loop principal da interface
menu_inicial.mainloop()
