# Verifica se as letras de uma palavra aparecem por ordem numa frase.

def subsequencia(palavra, frase):
    palavra = palavra.replace(" ", "").lower()
    frase = frase.replace(" ", "").lower()

    i = 0

    for letra in frase:
        if i < len(palavra) and letra == palavra[i]:
            i += 1

    return i == len(palavra)

print(subsequencia("palavra", "capa, lata, livro e caderno"))  # True
print(subsequencia("escondida", "mar, pesca, ondas e bebidas"))  # True
print(subsequencia("python", "programar em thonp y"))  # False
