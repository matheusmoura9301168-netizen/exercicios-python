# Calendário que não deixa escolher datas futuras.

from tkinter import Tk
from tkcalendar import Calendar
from datetime import date

janela = Tk()
janela.title("Calendário com limite de data")
hoje = date.today()
calendario = Calendar(
    janela,
    selectmode='day',
    maxdate=hoje,
    date_pattern='dd/mm/yyyy'
)
calendario.pack(padx=10, pady=10)

janela.mainloop()
