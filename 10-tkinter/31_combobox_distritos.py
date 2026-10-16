# Combobox com os distritos de Portugal e validação.

import tkinter as tk
from tkinter import ttk, messagebox

def validate_selection():

    selected_value = combobox.get()
    if selected_value not in predefined_options:
        messagebox.showerror("Erro", "Selecione uma opção!")
    else:
        messagebox.showinfo("Sucesso", f"Selecionou: {selected_value}")

# Configuração da janela principal
root = tk.Tk()
root.title("Seleção de Opções")
root.geometry("300x200")

# Opções pré-definidas
predefined_options = ["Aveiro", "Beja", "Braga", "Bragança", "Castelo Branco", "Coimbra", "Évora", "Faro", "Guarda", "Leiria", "Lisboa", "Portalegre", "Porto", "Santarém", "Setúbal", "Viana do Castelo", "Vila Real", "Viseu"]

# Frame para organizar os widgets
frame = ttk.Frame(root, padding=10)
frame.pack(fill='x', expand=True)

# Label e Combobox
combobox_label = ttk.Label(frame, text="Distrito:")
combobox_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

combobox = ttk.Combobox(frame, values=predefined_options, state="readonly", width=25)
combobox.set("Selecione...")  # Valor inicial
combobox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Botão para validar a seleção
validate_button = ttk.Button(root, text="Validar Seleção", command=validate_selection)
validate_button.pack(pady=10)

# Inicia o loop principal da interface
root.mainloop()
