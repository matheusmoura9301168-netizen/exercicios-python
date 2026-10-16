# Calcula a idade pelo ano de nascimento.

from datetime import date

ano_nas = int(input("Digite seu ano de nascimento: "))
anoatual = date.today().year
idade = anoatual - ano_nas

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
