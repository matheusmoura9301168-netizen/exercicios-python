# Os vários estilos de borda (relief) de um Label.

from tkinter import *

# Inicializa a janela principal
menu_inicial = Tk()
menu_inicial.title("Estilos de Relief")
menu_inicial.geometry("600x400")

# 🔹 Criação de labels com diferentes estilos de borda
Label(menu_inicial, text="solid", font="Arial 20", bd=10, relief="solid").pack()
Label(menu_inicial, text="groove", font="Arial 20", bd=10, relief="groove").pack()
Label(menu_inicial, text="flat", font="Arial 20", bd=10, relief="flat").pack()
Label(menu_inicial, text="raised", font="Arial 20", bd=10, relief="raised").pack()
Label(menu_inicial, text="sunken", font="Arial 20", bd=10, relief="sunken").pack()
Label(menu_inicial, text="ridge", font="Arial 20", bd=10, relief="ridge").pack()

# Inicia o loop principal da interface
menu_inicial.mainloop()
