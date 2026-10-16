# Controlo deslizante (Scale) que mostra o valor escolhido.

from tkinter import *

root = Tk()
root.geometry("300x200")
root.title("Controle deslizante")

#Função que mostra o valor atual do Scale
def vervalor(v):
    print(v)

# Criação do widget Scale
slide = Scale(root,
              from_=0,
              to=100,
              orient=HORIZONTAL,
              resolution=0.5,
              command=vervalor)
slide.pack(pady=20)

root.mainloop()
