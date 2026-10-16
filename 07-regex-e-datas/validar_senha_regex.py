# Regras de senha verificadas com regex.

import re


def val_pass(senha):
    a = 0
    if len(senha) < 4:
        print("Tamanho minimo de 4 caracteres")
    a = 1
    if len(re.findall(r"[A-Z]", senha)) < 1:
        print("Precisa conter 1 maiúsculas!")
    a = 1
    if len(re.findall(r"[a-z]", senha)) < 1:
        print("Precisa conter 1 minúsculas!")
    a = 1
    if len(re.findall(r"[@#$]", senha)) < 1:
        print("Precisa conter 1 dos caracteres especiais \"@ # $\"")
        a = 1
        return a
    else:
        return a


while True:

    senha1 = input("Introduza uma senha: ")
    a1 = val_pass(senha1)
    if a1 == 0:
        print("Senha válida")
    break
