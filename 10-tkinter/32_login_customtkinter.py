# Login com CustomTkinter em modo escuro.

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
janelahome = customtkinter.CTk()
janela = customtkinter.CTk()
janela.geometry("500x300")
janelahome.geometry("1280x720")


text = customtkinter.CTkLabel( janela, text="Login")
email = customtkinter.CTkEntry( janela, placeholder_text="Email")
password = customtkinter.CTkEntry( janela, placeholder_text="Password", show="*")
BotaoLogin = customtkinter.CTkButton(janela, text="Login", command=lambda: login(password.get()))
text.pack(padx=10 , pady=10)
email.pack(padx=10 , pady=10)
password.pack(padx=10 , pady=10)
BotaoLogin.pack(padx=10 , pady=10)


def login(senha):
    if senha == "1234":
        janela.destroy()
        janelahome.mainloop()
    else:
        mensagem = customtkinter.CTkLabel(janela, text="Senha incorreta", text_color="red")
        mensagem.pack(padx=10 , pady=3)
        mensagem.after(1500, mensagem.destroy)

text = customtkinter.CTkLabel( janelahome, text="Home")
text.pack(padx=10 , pady=10)




janela.mainloop()
