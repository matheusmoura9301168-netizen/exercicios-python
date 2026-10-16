# Formulário na consola que valida nome, data de nascimento e código de perfil.

import re
from datetime import datetime


def validar_nome(nome):
    if len(nome) > 55:
        return False, "O nome excede 55 caracteres."
    if re.search(r"\d", nome):
        return False, "O nome não pode conter números."
    if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
        return False, "O nome contém caracteres inválidos."
    return True, "Nome válido.\n"



def validar_data(data0):
    try:
        data = datetime.strptime(data0, "%d/%m/%Y")
        if data >= datetime.now():
            return False, "A data deve ser antes da data atual."
        return True, "Data válida."
    except ValueError:
        return False, "Formato inválido. Use DD/MM/AAAA.\n"



def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(padrao, email):
        return True, "Email válido."
    return False, "Email inválido.\n"



def validar_nif(nif):
    if not re.match(r"^\d{9}$", nif):
        return False, "O NIF deve conter exatamente 9 dígitos."
    pesos = [9,8,7,6,5,4,3,2]
    soma = sum(int(nif[i]) * pesos[i] for i in range(8))
    resto = soma % 11
    digito = 0 if resto < 2 else 11 - resto

    if digito == int(nif[-1]):
        return True, "NIF válido."
    return False, "NIF inválido (dígito de controlo incorreto).\n"



def validar_perfil(codigo):
    padrao = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{10,}$"
    if re.match(padrao, codigo):
        return True, "Código de perfil válido."
    return False, print("Código inválido.\n")


def formulario():

    while True:
        print("O Nome deve conter:\n"
              "- Maximo de 55 caracteres\n"
              "- Não pode conter números ou caracteres especiais.\n")
        nome = input("Nome completo: ")
        ok, msg = validar_nome(nome)
        print(msg)
        if ok:
            break

    while True:
        print("A Data deve conter:\n"
              "- Use o formato DD/MM/AAAA\n"
              "- A data deve ser antes da data atual.\n")
        data = input("Data de nascimento: ")
        ok, msg = validar_data(data)
        print(msg)
        if ok:
            break

    while True:
        print("O E-mail não deve conter:\n"
              "- Números ou caracteres especiais no inicio do e-mail.\n"
              "- Recomendação: Nome@Dominio.com\n")
        email = input("Email: ")
        ok, msg = validar_email(email)
        print(msg)
        if ok:
            break

    while True:
        print("A Data deve conter apenas números.\n")
        nif = input("NIF : ")
        ok, msg = validar_nif(nif)
        print(msg)
        if ok:
            break


    while True:
        print("A senha deve ter ao menos:\n"
                   "- 1 letra maiúscula\n"
                   "- 1 letra minúscula\n"
                   "- 1 número\n"
                   "- 1 símbolo\n"
                   "- mínimo de 10 caracteres")
        codigo = input("Código de Perfil (Senha): ")
        ok, msg = validar_perfil(codigo)
        print(msg)
        if ok:
            break

    print("\nPerfil validado com sucesso! 🎉🎉")
    print(f"Bem-vindo(a), {nome}!")

formulario()
