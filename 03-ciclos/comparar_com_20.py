# Conta, soma e faz a média dos números acima e abaixo de 20.

soma = 0
soma1 = 0
soma2 = 0
contador = 0
Cont1 = 0
Cont2 = 0
Cont3 = 0
while contador < 10:
    num = float(input("Introduza um numero: "))
    if num > 20:
        soma = soma + num
        contador = contador + 1
        Cont1 += 1
    elif num < 20:
        Cont2 += 1
        soma1 = soma1 + num
        contador = contador + 1
    else :
        soma2 = soma2 + num
        Cont3 += 1
        contador = contador + 1

media1 = soma1 / Cont2
media = soma / Cont1
print(f"numeros superiores a 20: {Cont1}")
print(f"numeros Inferiores a 20: {Cont2}")
print(f"numeros Iguais a 20: {Cont3}")
print(f"A média dos numeros superiores é: {media}")
print(f"A média dos numeros infriores é: {media1}")
print(f"A soma dos numeros superiores é: {soma}")
print(f"A soma dos numeros infriores é: {soma1}")
