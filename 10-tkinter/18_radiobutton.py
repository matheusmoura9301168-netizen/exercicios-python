# Escolha única com Radiobutton.

from tkinter import *

# Inicializa a janela principal
root = Tk()
root.title("Radiobuttons")
root.geometry("300x250")

# Frames para organizar os grupos
frameA = Frame(root)
frameA.pack(pady=10)

frameB = Frame(root)
frameB.pack(pady=10)

# Variáveis associadas aos grupos
valor_a = IntVar()
valor_b = IntVar()

# Radiobuttons do grupo A
ra_1 = Radiobutton(frameA, text="Opção A 1", variable=valor_a, value=1)
ra_2 = Radiobutton(frameA, text="Opção A 2", variable=valor_a, value=2)
ra_3 = Radiobutton(frameA, text="Opção A 3", variable=valor_a, value=3)

ra_1.pack(anchor=W)
ra_2.pack(anchor=W)
ra_3.pack(anchor=W)
ra_3.select()  # Seleciona a opção A 3 por padrão

# 🔹 Radiobuttons do grupo B
rb_1 = Radiobutton(frameB, text="Opção B 1", variable=valor_b, value=1)
rb_2 = Radiobutton(frameB, text="Opção B 2", variable=valor_b, value=2)
rb_3 = Radiobutton(frameB, text="Opção B 3", variable=valor_b, value=3)

rb_1.pack(anchor=W)
rb_2.pack(anchor=W)
rb_3.pack(anchor=W)

#Função que mostra o valor selecionado do grupo A
def ver_radio():
    print("Grupo A:", valor_a.get())
    print("Grupo B:", valor_b.get())

#Botão para executar a função
btn = Button(root, text="Executar", command=ver_radio)
btn.pack(pady=10)

# Inicia o loop principal da interface
root.mainloop()
