# Caixa de seleção e leitura do seu estado.

from tkinter import *

# Inicializa a janela principal
root = Tk()
root.title("Checkbox")

# Função que verifica o estado da checkbox
def apresentar():
    print(valor_check.get())  # 1 se marcada, 0 se desmarcada

# Variável associada à checkbox
valor_check = IntVar()

# Criação da checkbox
check = Checkbutton(
    root,
    text="Esta é uma checkbox.",
    variable=valor_check,
    command=apresentar
)
check.pack()

# Inicia o loop principal da interface
root.mainloop()
