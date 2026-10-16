# Escolha de horas e minutos com Spinbox.

import tkinter as tk
from tkinter import ttk, messagebox

def submit_time():
    hour = hour_spinbox.get()
    minute = minute_spinbox.get()
 #   am_pm = am_pm_combobox.get()
    if not hour.isdigit() or not minute.isdigit():
        messagebox.showerror("Erro", "Horas e minutos devem ser numéricos!")
        return

    selected_time = f"{hour}:{minute} " #devia estra dentro de aspas se usa-se Fuso horário {am_pm}
    messagebox.showinfo("Horário Selecionado", f"Agendou para as: {selected_time}")

# Configuração da janela principal
root = tk.Tk()
root.title("Seleção de Horário")
root.geometry("300x200")

# Frame para agrupar os widgets
frame = ttk.Frame(root, padding=10)
frame.pack(fill='x', expand=True)

# Label e Spinbox para horas
hour_label = ttk.Label(frame, text="Horas:")
hour_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
hour_spinbox = ttk.Spinbox(frame, from_=0, to=23, width=5, justify='center', wrap=True)
hour_spinbox.set("0")  # Valor inicial
hour_spinbox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Label e Spinbox para minutos
minute_label = ttk.Label(frame, text="Minutos:")
minute_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
minute_spinbox = ttk.Spinbox(frame, from_=0, to=59, width=5, justify='center', wrap=True, format="%02.0f")
minute_spinbox.set("00")  # Valor inicial
minute_spinbox.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Label e Combobox para AM/PM
'''am_pm_label = ttk.Label(frame, text="Período:")
am_pm_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
am_pm_combobox = ttk.Combobox(frame, values=["AM", "PM"], width=10, state="readonly", justify='center')
am_pm_combobox.set("AM")  # Valor inicial
am_pm_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="w")'''

# Botão para confirmar o horário
submit_button = ttk.Button(root, text="Confirmar Horário", command=submit_time)
submit_button.pack(pady=10)

# Inicia o loop principal da interface
root.mainloop()
