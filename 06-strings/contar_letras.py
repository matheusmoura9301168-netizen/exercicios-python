# Conta as letras de uma frase, sem espaços nem símbolos.

frase = input("Digite uma frase: ")

# Remove espaços da frase
frase_sem_espacos = frase.replace(" ", "")

# Conta apenas letras (ignorando números e símbolos)
contador = sum(1 for c in frase_sem_espacos if c.isalpha())

print(f"Número de letras (sem contar espaços):{contador}")
