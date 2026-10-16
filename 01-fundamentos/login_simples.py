# Guarda uma senha e pede-a de novo para fazer login.

from time import sleep

name = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

print("Olá {name} sua senha esta salva com sucesso.".format(name=name))

sleep(2)

senha1 = input("{nome} digite sua senha para login: ".format(nome=name))

if (senha1 == senha):
    print("senha correta")
else:
    print("senha incorreta.")
