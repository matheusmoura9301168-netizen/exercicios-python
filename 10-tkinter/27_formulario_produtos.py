# Formulário de produtos com cálculo do valor a pagar.

from tkinter import *

def validar_dados():
    try:
        codigo = text_codigo.get()
        nome_artigo = text_nome_artigo.get()
        preco = float(text_preco.get())
        quantidade = int(text_quantidade.get())

        # Calcular o valor antes do desconto
        valor_sem_desconto = preco * quantidade

        # Calcular o desconto (por exemplo, 10%)
        desconto_percentual = 10
        desconto = valor_sem_desconto * (desconto_percentual / 100)

        # Calcular o valor a pagar (com desconto)
        valor_a_pagar = valor_sem_desconto - desconto

        # Atualizar o Entry correspondente ao valor a pagar
        text_valor.delete(0, END)  # Limpar o conteúdo atual
        text_valor.insert(0, valor_a_pagar)

        # Faça o que quiser com os dados, por exemplo, imprimir no console
        print("Código:", codigo)
        print("Nome:", nome_artigo)
        print("Contacto:", preco)
        print("Cidade:", quantidade)
        print("desconto:", desconto)
        print("valor a pagar:", valor_a_pagar)

    except ValueError:
        print("Erro: Preço e quantidade devem ser números válidos!")
    except Exception as e:
        print("Erro inesperado:", e)

root = Tk()

frame_nome = Frame(root)
frame_morada = Frame(root)
label_codigo = Label(frame_nome, text="Código do Artigo: ")
label_nome_artigo = Label(frame_nome, text="Nome do Artigo: ")
label_preco = Label(frame_morada, text="Preço do Artigo: ")
label_quantidade = Label(frame_morada, text="Quantidade do Artigo: ")
label_valor = Label(frame_morada, text="Valor a Pagar: ")

text_codigo = Entry(frame_nome)
text_nome_artigo = Entry(frame_nome)
text_preco = Entry(frame_morada)
text_quantidade = Entry(frame_morada)
text_valor = Entry(frame_morada)

cmd_salvar = Button(root, text="Validar", command=validar_dados)

# layout
label_codigo.grid(row=0, column=0)
label_nome_artigo.grid(row=1, column=0)
text_codigo.grid(row=0, column=1)
text_nome_artigo.grid(row=1, column=1)

label_preco.grid(row=0, column=0)
label_quantidade.grid(row=1, column=0)
label_valor.grid(row=2, column=0)
text_preco.grid(row=0, column=1)
text_quantidade.grid(row=1, column=1)
text_valor.grid(row=2, column=1)

frame_nome.grid()
frame_morada.grid()

cmd_salvar.grid()
root.mainloop()
