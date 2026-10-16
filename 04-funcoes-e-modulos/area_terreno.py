# Área de um terreno com uma função.

def ar(larg, comp):
    return larg * comp

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
print(f"A área do terreno é {ar(largura, comprimento)} m²")
