# Listbox com seleção múltipla.

from tkinter import *

# Inicializa a janela principal
root = Tk()
root.title("Listbox Interativa")

# Criação da lista com seleção múltipla
lista = Listbox(root, selectmode=EXTENDED)
lista.pack(padx=10, pady=10)

# Inserção de itens a partir de uma lista
nomes = ['Joao', 'Ana', 'Carlos']
for nome in nomes:
    lista.insert(END, nome)

# Função para mostrar item(s) selecionado(s)
def executar():
    selecionados = lista.curselection()
    for i in selecionados:
        print(lista.get(i))

# Botão para ativar a função
cmd = Button(root, text="Clique", command=executar)
cmd.pack(pady=5)

# Exemplo de exclusão de item (Ana está no índice 1)
# lista.delete(1, 1)  # Descomente se quiser testar a remoção

# Inicia o loop principal da interface
root.mainloop()
