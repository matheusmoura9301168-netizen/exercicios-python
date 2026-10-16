# Label e Entry ligados a StringVar, atualizados por um botão.

from tkinter import *

#  Classe personalizada com Label, Entry e Button
class MinhaFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.label1_text = StringVar()
        self.text1_text = StringVar()

        #  Widgets
        self.label1 = Label(self, textvariable=self.label1_text)
        self.text1 = Entry(self, textvariable=self.text1_text)
        self.cmd1 = Button(self, text="Clique", command=self.Executar)

        #  Layout
        self.label1.grid(row=0, column=0, padx=5, pady=5)
        self.text1.grid(row=0, column=1, padx=5, pady=5)
        self.cmd1.grid(row=1, column=1, sticky=E, padx=5, pady=5)

    #  Método que atualiza o texto do label
    def Executar(self):
        nome = self.text1_text.get()
        self.label1_text.set(f"Olá, {nome}.")

# Janela principal
root = Tk()
root.geometry("300x150")
root.title("Saudação")

# Instanciando duas frames
frm1 = MinhaFrame(root)
frm1.grid(row=0, column=0, padx=10, pady=10)

frm2 = MinhaFrame(root)
frm2.grid(row=1, column=0, padx=10, pady=10)

# 🔹 Inicia o loop principal da interface
root.mainloop()
