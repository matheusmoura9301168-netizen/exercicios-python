# Texto em várias linhas com o widget Message.

from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Mensagem")

# Criação do widget Message
t = Message(root, text="Este é o texto do message widget.", width=200)
t.pack(pady=20)

root.mainloop()
