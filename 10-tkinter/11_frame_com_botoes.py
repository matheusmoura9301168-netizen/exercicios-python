# Frame com vários botões.

from tkinter import *

# Classe personalizada que herda de Frame
class FrameNome(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self['height'] = 100
        self['width'] = 250
        self['bd'] = 2
        self['relief'] = SOLID

        #  Botões dentro da frame
        self.btn1 = Button(self, text="Botão 1")
        self.btn2 = Button(self, text="Botão 2")

        # Layout dos botões
        self.btn1.grid(row=0, column=0, padx=10, pady=10)
        self.btn2.grid(row=0, column=1, padx=10, pady=10)

# principal
root = Tk()
root.title("App com Frames e Botões")

#  Instanciando múltiplas frames personalizadas
frame1 = FrameNome(root)
frame1.grid(row=0, column=0, padx=10, pady=10)

frame2 = FrameNome(root)
frame2.grid(row=1, column=0, padx=10, pady=10)

frame3 = FrameNome(root)
frame3.grid(row=2, column=0, padx=10, pady=10)

#  Inicia o loop principal da interface
root.mainloop()
