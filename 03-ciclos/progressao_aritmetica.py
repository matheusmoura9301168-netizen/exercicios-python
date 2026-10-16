# Termos e soma de uma progressão aritmética.

primeiro = int(input("Introduza o primeiro termo da PA: "))
razao = int(input("Introduza a razão da PA: "))
n = int(input("Introduza o número de termos: "))

soma = 0
print("Termos da PA:")

for i in range(n):
    termo = primeiro + i * razao
    print(termo)
    soma = soma + termo

print(f"A soma dos {n} termos é {soma}")
