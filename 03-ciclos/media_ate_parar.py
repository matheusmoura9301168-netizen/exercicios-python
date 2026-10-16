# Lê números até o utilizador responder N e mostra a média.

soma = 0
contador = 0

num = float(input("Introduza um número: "))
soma = soma + num
contador = contador + 1

resp = str(input("Quer continuar?[S/N] ")).upper().strip()[0]

while resp == "S":
    num = float(input("Introduza um número: "))
    soma = soma + num
    contador = contador + 1
    resp = str(input("Quer continuar?[S/N] ")).upper().strip()[0]

media = soma / contador
print("Foram introduzidos", contador, "números e a média é", round(media, 2))
