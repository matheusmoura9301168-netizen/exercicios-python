# Fatura com desconto conforme a quantidade comprada.

qtd = int(input("Digite a quantidade de produtos comprados: "))
valor_total = float(input("Digite o valor total da compra (sem desconto): "))

if qtd == 2:
    desconto = 0.02
elif 2 < qtd <= 5:
    desconto = 0.05
elif 5 < qtd < 10:
    desconto = 0.10
elif qtd >= 10:
    desconto = 0.15
else:
    desconto = 0.0

valor_desconto = valor_total * desconto
valor_com_desconto = valor_total - valor_desconto

print("\n   FATURA DA COMPRA")
print(f"Valor total (sem desconto): €{valor_total:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor do desconto: €{valor_desconto:.2f}")
print(f"Valor total (com desconto): €{valor_com_desconto:.2f}")
