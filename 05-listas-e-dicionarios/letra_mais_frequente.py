# Letra mais frequente de uma frase.

def LMC(texto):
    contagem = {}
    for letra in texto:
        if letra.isalpha():  # Ignora espaços e pontuação
            letra = letra.lower()
            contagem[letra] = contagem.get(letra, 0) + 1

    if not contagem:
        return None
    mais_frequente = max(contagem, key=contagem.get)
    return mais_frequente


entrada = input("Digite uma frase ou palavra: ")
resultado = LMC(entrada)
if resultado:
    print(f"A letra mais comum é: '{resultado}'")
else:
    print("Não foram encontradas letras.")
