# Texto justificado e propriedades do label.

from tkinter import *

# Inicializa a janela principal
menu_inicial = Tk()
menu_inicial.title("Exemplos de Label")
menu_inicial.geometry("600x400")

# Label com texto justificado à esquerda e anchor à esquerda
label1 = Label(
    menu_inicial,
    text="frase de testes\nteste",
    font="Arial 20",
    bd=1,
    relief="solid",
    width=30,
    height=5,
    justify=LEFT,   # Alinha múltiplas linhas à esquerda
    anchor=W        # Posiciona o bloco de texto à esquerda
)
label1.pack()

# Label com propriedades definidas diretamente na criação
label2 = Label(
    menu_inicial,
    text="frase de teste",
    font="Arial 20",
    bd=1,
    relief="solid"
)
label2.pack()

# Label com propriedades definidas após a criação
label3 = Label(menu_inicial)
label3['text'] = "texto da label2"
label3['font'] = "Arial 20"
label3['bd'] = 1
label3['relief'] = "solid"
label3.pack()

# Inicia o loop principal da interface
menu_inicial.mainloop()
