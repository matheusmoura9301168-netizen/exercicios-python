# Lista pendente com Combobox.

from tkinter import *
from tkinter import ttk

# Inicializa a janela principal
top = Tk()
top.geometry("200x150")
top.title("Combobox")

# Criação da frame para organização
frame = Frame(top)
frame.pack(pady=20)

# Lista de opções
langs = ["C", "C++", "Java", "Python", "PHP"]

# Criação da Combobox
Combo = ttk.Combobox(frame, values=langs)
Combo.set("Selecione a opção")  # Texto inicial
Combo.pack(padx=5, pady=5)

# Função para capturar seleção
def mostrar_opcao(event):
    print("Selecionado:", Combo.get())

# Evento de seleção
Combo.bind("<<ComboboxSelected>>", mostrar_opcao)

# Inicia o loop principal da interface
top.mainloop()
