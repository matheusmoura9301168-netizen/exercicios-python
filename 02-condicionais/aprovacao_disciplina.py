# Aprovação direta ou por exame.

nota = float(input("Digite sua nota em matemática: "))

if nota >= 10:
    print("Aprovado")
else:
    exame = float(input("Digite sua nota no exame: "))
    media = (nota + exame) / 2
    if media >= 10:
        print("Aprovado")
    else:
        print("Reprovado")
