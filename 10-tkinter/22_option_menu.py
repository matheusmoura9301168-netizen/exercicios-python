# Menu pendente (OptionMenu) que mostra a opção escolhida.

from tkinter import *

# Janela principal
root = Tk()
root.title("Dropdown interativo")
root.geometry("300x200")

# Frame para agrupar os widgets
f = Frame(root)
f.pack(pady=20)

#Variável e lista de opções
var = StringVar()
items = ["opção 1", "opção 2", "opção 3", "opção 4"]
var.set(items[1])  # Define opção inicial

# Dropdown (OptionMenu)
lista = OptionMenu(f, var, *items)
lista.config(font="Arial 18")
lista.pack()

#Label para mostrar a seleção
label = Label(f, font="Arial 12")
label.pack(pady=10)

#Botão que atualiza o label com a opção escolhida
def cmd():
    label.config(text=var.get())

botao = Button(f, text="Ok", font="Arial 14", command=cmd)
botao.pack()

#Inicia o loop principal
root.mainloop()
