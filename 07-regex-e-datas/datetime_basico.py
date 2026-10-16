# Exemplos com datetime, date e time.

from datetime import datetime, time, date
print("data e horas atuais")
dt = datetime.now()
print(dt)
print("year =", dt.year)
print("minute =", dt.month)
print("second =", dt.day)
print("hour =", dt.hour)
print("minute =", dt.minute)
print("second =", dt.second)
print("microsecond =", dt.microsecond)
print("data")
dt1=date(2023,5,20)
print(dt1)
print("dia =", dt1.day)
print("mês =", dt1.month)
print("ano =", dt1.year)
print("\nTempo")
Time = time(11, 34, 56)
print(Time)
print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)

'''
Através do módulo datetime, com o uso da
classe date e dos métodos today() e strftime()
'''
from datetime import date
data_em_texto = date.today().strftime('\n\n%d/%m/%Y')
print(data_em_texto)
