# Índice de massa corporal a partir do peso e da altura.

p = float(input("Peso (kg): "))
a = float(input("Altura (m): "))
if a <= 0:
    print("A altura tem de ser maior que zero.")
else:
    print(f"IMC: {p / (a * a):.2f}")
