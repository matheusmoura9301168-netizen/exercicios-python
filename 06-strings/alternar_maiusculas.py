# Alterna maiúsculas e minúsculas numa palavra.

def AUD(palavra):
    resultado = ""
    for i, letra in enumerate(palavra):
        if i % 2 == 0:
            resultado = resultado + letra.upper()
        else:
            resultado = resultado + letra.lower()
    return resultado


entrada = input("Digite uma palavra: ")
print("Formato alternado:", AUD(entrada))
