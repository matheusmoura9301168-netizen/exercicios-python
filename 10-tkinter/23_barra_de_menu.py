# Barra de menus no topo da janela.

from tkinter import *

# Funções associadas aos comandos do menu
def abrir():
    print("abrir")

def salvar():
    print("salvar")

def ajuda():
    print("ajuda")

#Janela principal
top = Tk()
top.title("Menu Exemplo")
top.geometry("300x200")

#Menu principal
principal = Menu(top)

# Submenu "Arquivo"
arquivo = Menu(principal, tearoff=0)
arquivo.add_command(label="Abrir", command=abrir)
arquivo.add_command(label="Salvar", command=salvar)
principal.add_cascade(label="Arquivo", menu=arquivo)

# Comando direto "Ajuda"
principal.add_command(label="Ajuda", command=ajuda)

# Aplica o menu à janela
top.config(menu=principal)

#Inicia o loop principal
top.mainloop()
