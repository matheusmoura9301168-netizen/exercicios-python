# Percentagem de alunos de cada sexo numa turma.

# Receber os dados
talunos = int(input("Digite o número total de alunos: "))
tmasc = int(input("Digite o número de alunos do sexo masculino: "))

if talunos <= 0:
    print("O número total de alunos tem de ser maior que zero.")
    raise SystemExit

# Imprimir as percentagens diretamente
print("Percentagem de alunos do sexo masculino:", (tmasc / talunos) * 100, "%")
print("Percentagem de alunos do sexo feminino:", ((talunos - tmasc) / talunos) * 100, "%")
