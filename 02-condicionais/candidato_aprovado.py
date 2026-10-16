# Verifica se um candidato cumpre idade, nota e escolaridade.

idade = int(input("Digite sua idade: "))
nota = int(input("Digite sua nota no exame de matemática: "))
secundario = input("Terminou o secundário? (s/n): ").lower() == 's'

if idade < 25 and nota >= 140 and secundario:
    print("Candidato aprovado")
else:
    print("Candidato não aprovado")
