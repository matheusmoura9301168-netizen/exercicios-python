# Verifica os requisitos de idade e experiência para uma vaga.

idade = int(input("Digite sua idade: "))
experiencia = int(input("Digite seus anos de experiência: "))

if idade < 55 or experiencia >= 5 or (idade > 55 and experiencia >= 10):
    print("Candidato habilitado à vaga")
else:
    print("Candidato não habilitado à vaga")
