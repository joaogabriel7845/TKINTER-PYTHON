import customtkinter as ctk

# Configuração aparência
ctk.set_appearance_mode('dark')


# Criação das funções de funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # Verificar se o usuario é dogcore e a senha 123456
    if usuario == 'dogcore' and senha == '123456':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Login incorreto !', text_color='red')

# Criação da janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

#  Criação dos labels
# label -> texto dentro da janela
label_usuario = ctk.CTkLabel(app, text='Usuário:', padx=10, pady=10)
label_usuario.pack(pady=10)

# entry
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app, text='Senha:', padx=10, pady=10)
label_senha.pack(pady=10)

# entry
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

# button -> cria um botão na janela com base em alguma funcionalidade
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

# campo feedback de login
resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)

# Iniciar a aplicação
app.mainloop()