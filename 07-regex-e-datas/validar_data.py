# Aceita datas com / ou - e verifica se são válidas.

from datetime import datetime

while True:
    data_str = input("Digite uma data (dd/mm/yyyy ou dd-mm-yyyy): ")
    try:
        if "/" in data_str:
            data = datetime.strptime(data_str, "%d/%m/%Y")
        else:
            data = datetime.strptime(data_str, "%d-%m-%Y")
        print("Data válida:", data.strftime("%d/%m/%Y"))
        break
    except ValueError:
        print("Data inválida. Tente novamente.")
