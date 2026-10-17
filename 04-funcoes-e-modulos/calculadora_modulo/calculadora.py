# Módulo com as quatro operações.

# Esse módulo realiza as 4 operações matemáticas
# Recebe dois números e retorna a soma
def soma(x,y):
    return x+y
# Recebe dois números e retorna a diferença
def subtracao(x,y):
    return x-y
# Recebe dois números e retorna o produto
def multiplicacao(x,y):
    return x*y
# Recebe dois números e retorna a divisão do primeiro pelo segundo
def divisao(x,y):
    if y == 0:
        return "não é possível dividir por zero"
    return x/y
