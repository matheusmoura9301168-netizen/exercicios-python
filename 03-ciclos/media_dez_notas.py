# Média de 10 notas entre 0 e 20, com validação.

soma = 0
contador = 0

while contador < 10:
    nota = float(input("Introduza a nota do aluno " + str(contador+1) + ": "))
    if 0 <= nota <= 20:
        soma = soma + nota
        contador = contador + 1
    else:
        print("Nota inválida! Introduza um valor entre 0 e 20.")

media = soma / 10
print("A média das notas é", round(media, 2))
