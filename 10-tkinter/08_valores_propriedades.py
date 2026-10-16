# Mostra cada propriedade do Label com o seu valor.

from tkinter import *

# Inicializa a janela principal
menu_inicial = Tk()
menu_inicial.title("Propriedades da Label")

# Cria uma label simples
label1 = Label(menu_inicial, text="Menu Principal")
label1.pack()

#  Imprime todas as chaves e seus valores associados
for item in label1.keys():
    print(item, ":", label1[item])

# Inicia o loop principal da interface
menu_inicial.mainloop()
