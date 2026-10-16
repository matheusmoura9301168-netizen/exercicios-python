# Alinhamento do texto dentro de um Label com anchor.

from tkinter import *

# Inicializa a janela principal
menu_inicial = Tk()
menu_inicial.title("Alinhamento com Anchor")
menu_inicial.geometry("600x300")

# Label com texto alinhado no canto superior esquerdo (NW = North-West)
Label(menu_inicial,
      text="0123456789",
      font="Arial 20",
      bd=1,
      relief="solid",
      width=25,
      height=4,
      anchor=NW).pack()

# Label com texto centralizado (CENTER)
Label(menu_inicial,
      text="0123456789",
      font="Arial 20",
      bd=1,
      relief="solid",
      width=25,
      height=4,
      anchor=CENTER).pack()

# Inicia o loop principal da interface
menu_inicial.mainloop()
