# Quantidade e preço com validação e total a pagar.

import tkinter as tk
from tkinter import ttk, messagebox


def calcular_total():

    try:
        quantidade = int(spinbox.get())  # Obtém a quantidade inserida no Spinbox
        if quantidade < 1 or quantidade > 100:
            messagebox.showerror("Erro", "Quantidade deve estar entre 1 e 100.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira uma quantidade válida.")
    try:
        # Obtém o preço inserido na Entry
        preco_unitario = float(preco_entry.get())
        if preco_unitario <= 0:
            messagebox.showerror("Erro", "O preço deve ser um valor positivo.")
            return

        total = quantidade * preco_unitario  # Calcula o total
        resultado_label.config(text=f"Total a pagar: {total:.2f} Euros")  # Exibe o total
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira preços válidos.")


# Configuração da janela principal
root = tk.Tk()
root.title("Venda de Produtos")
root.geometry("350x250")

# Frame para organizar os widgets
frame = ttk.Frame(root, padding=10)
frame.pack(fill='x', expand=True)

# Label e Spinbox para quantidade
quantidade_label = ttk.Label(frame, text="Quantidade de Produto:")
quantidade_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Spinbox para selecionar a quantidade (de 1 a 10)
spinbox = ttk.Spinbox(frame, from_=1, to=100, width=10)
spinbox.grid(row=0, column=1, padx=5, pady=5)

# Label e Entry para o preço
preco_label = ttk.Label(frame, text="Preço do Produto (Euros):")
preco_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

preco_entry = ttk.Entry(frame, width=10)
preco_entry.grid(row=1, column=1, padx=5, pady=5)

# Botão para calcular o total
calcular_button = ttk.Button(root, text="Calcular Total", command=calcular_total)
calcular_button.pack(pady=10)

# Label para exibir o total
resultado_label = ttk.Label(root, text="Total a pagar:", font=("Arial", 12))
resultado_label.pack(pady=10)

# Inicia o loop principal da interface
root.mainloop()
